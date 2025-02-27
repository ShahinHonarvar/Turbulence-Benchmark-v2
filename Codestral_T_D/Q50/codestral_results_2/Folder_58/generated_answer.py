from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for s in lst:
        if len(s) >= 3:
            counter[tuple(sorted(s.lower()))] += 1
    return sum((v * (v - 1) // 2 for v in counter.values())) >= 411