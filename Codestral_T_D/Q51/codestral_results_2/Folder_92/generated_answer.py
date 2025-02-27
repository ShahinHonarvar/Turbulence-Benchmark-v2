from collections import defaultdict

def if_contains_anagrams(strings):
    d = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            key = ''.join(sorted(s))
            d[key].append(s)
    count = sum((len(v) * (len(v) - 1) // 2 for v in d.values()))
    return count <= 34