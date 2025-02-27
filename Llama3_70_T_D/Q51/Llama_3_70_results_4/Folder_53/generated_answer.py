from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] += 1
    return sum((1 for v in anagrams.values() if v > 1)) <= 8