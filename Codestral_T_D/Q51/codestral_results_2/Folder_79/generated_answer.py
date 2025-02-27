from collections import defaultdict

def if_contains_anagrams(strings):
    d = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            key = ''.join(sorted(s))
            d[key] += 1
    return sum((v * (v - 1) // 2 for v in d.values())) <= 173