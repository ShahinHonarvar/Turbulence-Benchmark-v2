from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            anagrams[''.join(sorted(s))].append(s)
    count = sum((1 for v in anagrams.values() if len(v) > 1))
    return count >= 140