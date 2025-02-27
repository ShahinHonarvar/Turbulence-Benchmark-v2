from heapq import nsmallest

def find_n_th_smallest_num(nums):
    return nsmallest(16, nums)[15]