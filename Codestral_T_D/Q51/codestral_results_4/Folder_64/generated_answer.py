from collections import Counter

def if_contains_anagrams(strings):
    counts = Counter()
    for s in strings:
        if len(s) >= 3:
            key = tuple(sorted(s.lower()))
            counts[key] += 1
    return sum((n * (n - 1) // 2 for n in counts.values())) <= 59