from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_groups = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            anagram_groups[''.join(sorted(string.lower()))].append(string)
    count = 0
    for key in anagram_groups:
        if len(anagram_groups[key]) >= 2:
            count += len(anagram_groups[key]) * (len(anagram_groups[key]) - 1) / 2
    return count >= 26