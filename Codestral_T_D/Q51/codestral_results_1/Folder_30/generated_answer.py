from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        key = ''.join(sorted(s))
        d[key].append(s)
    count = 0
    for key in d:
        if len(d[key]) > 1:
            count += len(d[key]) * (len(d[key]) - 1) // 2
    return count <= 28