from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_groups = defaultdict(list)
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_groups[sorted_string].append(string)
    count = 0
    for key in anagram_groups:
        group_len = len(anagram_groups[key])
        if group_len > 1:
            count += group_len * (group_len - 1) // 2
    if count > 17:
        return False
    else:
        return True