from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_tuple = tuple(sorted(string.lower()))
            anagram_groups[sorted_tuple].append(string)
    for group in anagram_groups.values():
        if len(group) > 1:
            anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count >= 39