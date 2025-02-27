from collections import Counter

def if_contains_anagrams(strings):
    counts = Counter((''.join(sorted(s.lower())) for s in strings if len(s) >= 3 and s.isalpha()))
    return sum((c * (c - 1) // 2 for c in counts.values())) <= 40