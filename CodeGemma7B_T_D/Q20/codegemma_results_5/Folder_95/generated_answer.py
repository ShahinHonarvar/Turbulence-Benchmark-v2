from heapq import heappush, heappop

def find_n_th_smallest_num(nums):
    min_heap = []
    for i in range(44, 49):
        heappush(min_heap, nums[i])
    for i in range(5):
        heappop(min_heap)
    return min_heap[0]