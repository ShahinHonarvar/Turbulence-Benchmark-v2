from collections import Counter

def if_contains_anagrams(strings):
    sanitized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_pairs = 0
    counter = Counter(sanitized_strings)
    for count in counter.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 34:
                return False
    return anagram_pairs <= 34