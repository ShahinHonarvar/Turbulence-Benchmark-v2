from collections import defaultdict
    from math import comb

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    total_pairs = 0
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] += 1
    for count in anagrams.values():
        total_pairs += comb(count, 2)
    return total_pairs <= 318