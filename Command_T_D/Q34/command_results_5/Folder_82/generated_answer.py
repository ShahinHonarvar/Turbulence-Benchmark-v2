import heapq
    import collections

def find_original_set(S):
    s = set(S)
    s = list(s)
    s.sort()
    heapq.heapify(s)
    cur = collections.defaultdict(list)
    for x in s:
        cur[x].append(x)
    m = len(s)
    return s[:m]