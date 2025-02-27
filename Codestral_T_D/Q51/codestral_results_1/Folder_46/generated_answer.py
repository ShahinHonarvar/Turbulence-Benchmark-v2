from collections import Counter

def if_contains_anagrams(strings):
    anagram_counts = Counter((tuple(sorted(s.lower())) for s in strings if len(s) >= 3))
    return sum((v * (v - 1) // 2 for v in anagram_counts.values())) <= 61