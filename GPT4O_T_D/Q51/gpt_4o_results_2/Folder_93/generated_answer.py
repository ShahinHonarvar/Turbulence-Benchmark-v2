from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    counter = Counter(normalized_strings)
    for count in counter.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
        if anagram_count > 36:
            return False
    return True