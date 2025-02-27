from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for s in strings:
        if len(s) >= 3:
            counter[frozenset(Counter(s.lower()))] += 1
    return sum((v * (v - 1) // 2 for v in counter.values())) <= 38