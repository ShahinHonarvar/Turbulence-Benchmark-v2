import heapq

def return_n_smallest_chars(s):
    n = 36
    sorted_chars = heapq.nsmallest(n, s)
    return sorted_chars