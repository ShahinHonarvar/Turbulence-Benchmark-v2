from collections import defaultdict

def if_contains_anagrams(strings):
    d = defaultdict(list)
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            d[key].append(s)
    count = 0
    for key in d:
        if len(d[key]) > 1:
            count += len(d[key]) * (len(d[key]) - 1) // 2
    return count <= 59