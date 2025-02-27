from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams_count = defaultdict(int)
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            anagrams_count[sorted_str] += 1
    pairs_count = sum((v * (v - 1) // 2 for v in anagrams_count.values()))
    return pairs_count <= 72