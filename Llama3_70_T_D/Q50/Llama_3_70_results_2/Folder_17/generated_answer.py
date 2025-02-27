from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams_count = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams_count[sorted_s] += 1
    pairs = 0
    for k, v in anagrams_count.items():
        if v > 1:
            pairs += v * (v - 1) // 2
    return pairs >= 97