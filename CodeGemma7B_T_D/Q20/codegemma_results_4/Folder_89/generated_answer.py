from heapq import heappop, heappush

def find_n_th_smallest_num(nums):
    min_heap = nums[11:54]
    for num in min_heap:
        heappush(min_heap, num)
    for _ in range(19):
        heappop(min_heap)
    return heappop(min_heap)