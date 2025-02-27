from collections import Counter

def if_contains_anagrams(strings):
    counts = Counter((tuple(sorted(s.lower())) for s in strings if len(s) >= 3))
    return sum((v * (v - 1) // 2 for v in counts.values())) <= 92