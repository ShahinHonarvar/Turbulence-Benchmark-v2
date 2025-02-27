from heapq import heappop, heappush

def find_second_smallest_num(num_list):
    heap = []
    for num in num_list[26:]:
        heappush(heap, num)
    if len(heap) < 2:
        return None
    heappop(heap)
    return heappop(heap)