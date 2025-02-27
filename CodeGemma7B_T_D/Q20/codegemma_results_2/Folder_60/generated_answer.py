import heapq

def find_n_th_smallest_num(nums):
    unique_nums = set(nums)
    min_heap = []
    for num in sorted(unique_nums):
        heapq.heappush(min_heap, num)
    for _ in range(n - 1):
        heapq.heappop(min_heap)
    if min_heap:
        return heapq.heappop(min_heap)
    return None