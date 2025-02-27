from heapq import heappush, heappop

def find_n_th_smallest_num(nums):
    min_heap = []
    for num in nums[:4]:
        heappush(min_heap, num)
    for num in nums[4:]:
        if num < min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, num)
    return min_heap[0]