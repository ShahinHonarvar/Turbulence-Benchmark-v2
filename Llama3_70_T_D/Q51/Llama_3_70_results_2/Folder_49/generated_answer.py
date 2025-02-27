from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for s in lst:
        lower_s = ''.join(filter(str.isalpha, s.lower()))
        if len(lower_s) < 3:
            continue
        sorted_s = ''.join(sorted(lower_s))
        anagrams[sorted_s] += 1
    count = sum((1 for v in anagrams.values() if v > 1))
    return count <= 10