from heapq import heappop, heappush

def find_n_th_smallest_num(num_list):
    min_heap = []
    for i in range(11, 25):
        heappush(min_heap, num_list[i])
    for i in range(25, len(num_list)):
        if min_heap[0] > num_list[i]:
            heappop(min_heap)
            heappush(min_heap, num_list[i])
    return heappop(min_heap)