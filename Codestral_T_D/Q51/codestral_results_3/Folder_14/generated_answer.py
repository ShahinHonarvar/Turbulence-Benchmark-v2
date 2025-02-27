from collections import Counter

def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            key = ''.join(sorted(lower_string))
            if key not in anagram_groups:
                anagram_groups[key] = []
            anagram_groups[key].append(lower_string)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return anagram_pairs <= 474