from collections import Counter

def if_contains_anagrams(strings):
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_pairs = sum((v * (v - 1) // 2 for v in Counter(normalized_strings).values()))
    return anagram_pairs >= 14