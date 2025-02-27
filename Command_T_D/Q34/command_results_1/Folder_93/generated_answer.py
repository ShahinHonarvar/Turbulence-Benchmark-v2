import sys
    from heapq import heapify, heappop

def find_original_set(s):
    hq = []
    for x in s:
        if x not in hq:
            heapify(hq)
            hq.append(x)
    hq.sort()
    x = set()
    while hq:
        s = heappop(hq)
        for i in range(len(s)):
            if s[i] not in x:
                x.add(s[i])
        if x == s:
            return x
    return x