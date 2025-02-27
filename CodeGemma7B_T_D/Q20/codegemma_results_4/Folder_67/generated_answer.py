from heapq import nsmallest

def find_n_th_smallest_num(nums):
    return nsmallest(n=7, iterable=nums[23:45])[6]