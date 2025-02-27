from collections import Counter

def if_contains_anagrams(strings):
    counts = Counter((tuple(sorted(s.lower())) for s in strings if len(s) >= 3))
    return any((count >= 2 for count in counts.values() if count >= 106))