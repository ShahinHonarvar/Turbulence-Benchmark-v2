import heapq

def find_n_th_smallest_num(nums):
    return heapq.nlargest(14, nums)[32:61]