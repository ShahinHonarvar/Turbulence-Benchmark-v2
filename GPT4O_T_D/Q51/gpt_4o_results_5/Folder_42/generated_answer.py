from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    string_count = Counter(sorted_strings)
    for count in string_count.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 38:
                return False
    return True