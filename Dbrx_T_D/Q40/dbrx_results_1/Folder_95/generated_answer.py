import heapq

def return_n_smallest_chars(s):
    ordered_chars = heapq.nsmallest(36, s)
    return ordered_chars