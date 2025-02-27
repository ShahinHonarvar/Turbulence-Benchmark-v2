from heapq import heappop, heappush

def find_n_th_smallest_num(nums):
    min_heap = []
    for num in nums:
        heappush(min_heap, num)
    for _ in range(4):
        heappop(min_heap)
    res = []
    for _ in range(5):
        res.append(heappop(min_heap))
    return res