import sys
import heapq as hq

def find_original_set(x):
    sys.setrecursionlimit(10 ** 5)
    m = set()
    for i in range(len(x)):
        j = i
        while j < len(x):
            m.add(x[j])
            j += 1
    return m