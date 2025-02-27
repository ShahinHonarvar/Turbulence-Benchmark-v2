from heapq import heappop, heappush

def find_second_smallest_num(num_list):
    min_heap = []
    for i in range(11, 101):
        if num_list[i] is not None:
            heappush(min_heap, num_list[i])
            if len(min_heap) > 2:
                heappop(min_heap)
    if len(min_heap) >= 2:
        return heappop(min_heap)
    else:
        return 'None'