from heapq import heappop, heappush

def find_n_th_smallest_num(nums):
    min_heap = []
    for num in nums:
        heappush(min_heap, num)
    for _ in range(len(nums) - 11):
        heappop(min_heap)
    return heappop(min_heap)