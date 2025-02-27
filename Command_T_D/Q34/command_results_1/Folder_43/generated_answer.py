import sys
import heapq

def find_original_set(s):
    heapq.heapify(s)
    while s:
        s.pop()
        s = set.union(s)
    return s