from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_groups = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_groups[sorted_string].append(string)
    count_pairs = 0
    for group in anagram_groups.values():
        group_size = len(group)
        if group_size >= 2:
            count_pairs += group_size * (group_size - 1) // 2
    return count_pairs >= 81