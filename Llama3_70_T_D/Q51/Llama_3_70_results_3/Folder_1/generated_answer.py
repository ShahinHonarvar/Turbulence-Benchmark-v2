from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams_count = defaultdict(int)
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams_count[sorted_s] += 1
    count = sum((1 for v in anagrams_count.values() if v > 1))
    return count <= 30