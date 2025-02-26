from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    anagram_count = 0
    for s in string_list:
        s_filtered = ''.join(filter(str.isalpha, s.lower()))
        if len(s_filtered) >= 3:
            sorted_s = ''.join(sorted(s_filtered))
            anagram_dict[sorted_s].append(s)
    for anagram_group in anagram_dict.values():
        group_size = len(anagram_group)
        if group_size > 1:
            anagram_count += group_size * (group_size - 1) // 2
        if anagram_count > 42:
            return False
    return True