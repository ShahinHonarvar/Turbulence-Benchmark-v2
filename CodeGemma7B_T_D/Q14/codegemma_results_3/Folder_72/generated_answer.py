from heapq import heappush, heappop

def find_second_smallest_num(nums):
    if len(nums) < 87:
        return None
    min_heap = []
    for i in range(82, 87):
        heappush(min_heap, nums[i])
    return heappop(min_heap)