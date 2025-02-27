from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        anagrams[sorted_s] += 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pairs <= 55