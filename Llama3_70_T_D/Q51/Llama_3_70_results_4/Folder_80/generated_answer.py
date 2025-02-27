from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        d[sorted_s] += 1
    pairs = sum((v * (v - 1) // 2 for v in d.values()))
    return pairs <= 255