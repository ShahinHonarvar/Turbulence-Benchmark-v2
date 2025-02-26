from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for s in string_list:
        s_lower = ''.join((c.lower() for c in s if c.isalpha()))
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagram_dict[sorted_s].append(s)
    for group in anagram_dict.values():
        if len(group) > 1:
            anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count <= 54