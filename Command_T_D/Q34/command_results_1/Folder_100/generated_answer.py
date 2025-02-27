import sys
    from collections import defaultdict

def find_original_set(s):
    s = set(s)
    d = defaultdict(set)
    for i in s:
        d[i].add(i)
    s = set()
    for i in d:
        s.update(d[i])
    return s