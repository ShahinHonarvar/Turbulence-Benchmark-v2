from collections import defaultdict

def if_contains_anagrams(strs):
    d = defaultdict(list)
    for s in strs:
        if len(s) >= 3:
            key = ''.join(sorted((c.lower() for c in s)))
            d[key].append(s)
    return max((len(v) for v in d.values())) <= 392