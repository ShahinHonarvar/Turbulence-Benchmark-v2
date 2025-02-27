from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_groups = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_groups[sorted_string].append(string)
    count = 0
    for key, value in anagram_groups.items():
        group_size = len(value)
        if group_size >= 2:
            count += group_size * (group_size - 1) // 2
    return count >= 38