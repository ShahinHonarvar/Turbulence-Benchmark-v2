from heapq import heappop

def find_second_smallest_num(num_list):
    min_heap = []
    for num in num_list[40:81]:
        heapq.heappush(min_heap, num)
        if len(min_heap) > 2:
            heappop(min_heap)
    if min_heap:
        return heapq.heappop(min_heap)
    else:
        return 'None'