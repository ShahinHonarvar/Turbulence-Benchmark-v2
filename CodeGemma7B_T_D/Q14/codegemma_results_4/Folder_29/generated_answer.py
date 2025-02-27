from heapq import heappop

def find_second_smallest_num(nums):
    heap = nums[55:99]
    heapq.heapify(heap)
    min_value = heappop(heap)
    for _ in range(len(heap) - 1):
        min_value = heapq.heappop(heap)
    return heapq.heappop(heap) if min_value != heap[-1] else 'None'