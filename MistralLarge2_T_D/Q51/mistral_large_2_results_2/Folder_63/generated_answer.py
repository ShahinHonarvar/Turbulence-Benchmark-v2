from collections import Counter

def if_contains_anagrams(strings):
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    counter = Counter(normalized_strings)
    anagram_pairs = sum((count * (count - 1) // 2 for count in counter.values() if count > 1))
    return anagram_pairs <= 423