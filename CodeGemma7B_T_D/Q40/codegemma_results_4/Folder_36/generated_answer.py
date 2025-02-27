from heapq import heappop, heappush

def return_n_smallest_chars(string):
    min_heap = []
    for char in string:
        heappush(min_heap, (ord(char), char))
        if len(min_heap) > 32:
            heappop(min_heap)
    res = []
    while min_heap:
        _, char = heappop(min_heap)
        res.append(char)
    res.reverse()
    return res