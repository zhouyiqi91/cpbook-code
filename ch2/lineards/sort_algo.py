import random
from math import inf

def merge_sort(A,lo,hi):
    def merge(lo,mid,hi):
        L = A[lo:mid+1].copy()
        R = A[mid+1:hi+1].copy()
        L.append(inf)
        R.append(inf)
        i = j = 0
        for k in range(lo,hi+1):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
        
    if lo < hi:
        mid = lo+hi>>1
        merge_sort(A, lo, mid)
        merge_sort(A, mid+1, hi)
        merge(lo,mid,hi)

def swap(A,i,j):
    A[i],A[j] = A[j], A[i]

def quick_sort(A,lo,hi):
    def partition(lo,hi):
        pivot = A[hi]
        i = lo-1
        for j in range(lo,hi):
            if A[j] < pivot or (A[j]==pivot and j % 2==0):
                i += 1
                swap(A,i,j)
        swap(A,i+1,hi)
        return i+1

    if lo<hi:
        mid = partition(lo,hi)
        quick_sort(A,lo,mid-1)
        quick_sort(A,mid+1,hi)
    
        

if __name__ == '__main__':
    n = 1000
    nums = [random.randint(1,10000) for _ in range(n)]
    a = sorted(nums)
    quick_sort(nums,0,len(nums)-1)
    print(nums)
    assert(a==nums) 