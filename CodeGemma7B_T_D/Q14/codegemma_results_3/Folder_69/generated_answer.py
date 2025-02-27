from heapq import heappop, heappush

def find_second_smallest_num(nums):
    min_heap = nums[25:88]
    heappush(min_heap, float('inf'))
    while len(min_heap) > 2:
        heappop(min_heap)
    if len(min_heap) < 2:
        return None
    return heappop(min_heap)