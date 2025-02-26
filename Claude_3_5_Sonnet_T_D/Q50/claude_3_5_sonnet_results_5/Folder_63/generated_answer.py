from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for s in string_list:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s].append(s)
    for anagram_group in anagram_dict.values():
        group_size = len(anagram_group)
        if group_size > 1:
            anagram_count += group_size * (group_size - 1) // 2
    return anagram_count >= 89