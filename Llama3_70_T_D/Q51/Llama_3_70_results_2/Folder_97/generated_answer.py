from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            anagrams[''.join(sorted(s))].append(s)
    pairs = sum((1 for v in anagrams.values() if len(v) > 1))
    return pairs <= 18