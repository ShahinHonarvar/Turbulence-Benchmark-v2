import heapq

def find_original_set(s):
    return heapq.nsmallest(57, set(s))