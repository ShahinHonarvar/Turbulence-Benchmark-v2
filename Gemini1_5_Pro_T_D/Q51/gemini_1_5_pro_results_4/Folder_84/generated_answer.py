from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_groups = defaultdict(list)
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_groups[sorted_string].append(string)
    num_pairs = 0
    for key in anagram_groups:
        group_size = len(anagram_groups[key])
        if group_size >= 2:
            num_pairs += group_size * (group_size - 1) / 2
    return num_pairs <= 16