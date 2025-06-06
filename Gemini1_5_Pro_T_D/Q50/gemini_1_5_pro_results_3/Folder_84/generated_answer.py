from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_groups = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            anagram_groups[''.join(sorted(string.lower()))].append(string)
    count = 0
    for key in anagram_groups:
        group_size = len(anagram_groups[key])
        if group_size >= 2:
            count += group_size * (group_size - 1) // 2
    if count >= 108:
        return True
    else:
        return False