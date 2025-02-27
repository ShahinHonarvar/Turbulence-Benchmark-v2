import sys
import heapq

def find_original_set(S):
    sets = [set(x) for x in S]
    heap = []
    for x in sets:
        heapq.heappush(heap, x)
    original_set = set()
    while heap:
        set_ = heapq.heappop(heap)
        if set_.issubset(original_set):
            break
        original_set.update(set_)
    return original_set