from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_groups = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_groups[sorted_string].append(string)
    count = 0
    for key in anagram_groups:
        group_length = len(anagram_groups[key])
        if group_length >= 2:
            count += group_length * (group_length - 1) // 2
    return count >= 16