from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_map[sorted_string].append(string)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_map.values()))
    return anagram_pairs <= 36