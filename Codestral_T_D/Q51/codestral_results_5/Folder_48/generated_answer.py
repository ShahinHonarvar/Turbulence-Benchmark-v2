from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            d[key].append(s)
    count = 0
    for key in d.keys():
        if len(d[key]) >= 2:
            count += len(d[key]) * (len(d[key]) - 1) // 2
    return count <= 277