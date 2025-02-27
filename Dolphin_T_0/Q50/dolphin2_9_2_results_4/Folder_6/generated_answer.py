from collections import Counter

def if_contains_anagrams(lst):
    cnt = Counter()
    for s in lst:
        if len(s) >= 3:
            cnt[tuple(sorted(s.lower()))] += 1
    return any((v >= 2 for v in cnt.values()))