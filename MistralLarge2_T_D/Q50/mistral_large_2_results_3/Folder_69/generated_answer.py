from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    anagram_pairs = 0
    for group in anagram_dict.values():
        if len(group) > 1 and len(group[0]) >= 3:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs >= 188