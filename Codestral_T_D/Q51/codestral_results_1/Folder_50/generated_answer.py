from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            counter[tuple(sorted(s))] += 1
    return sum((v * (v - 1) // 2 for v in counter.values())) <= 47