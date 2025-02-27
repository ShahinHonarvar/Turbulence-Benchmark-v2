from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    count_dict = Counter(normalized_strings)
    for count in count_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
        if anagram_count >= 35:
            return True
    return False