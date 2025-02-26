from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    anagram_count = 0
    for s in string_list:
        s_lower = ''.join(filter(str.isalpha, s.lower()))
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagram_dict[sorted_s].append(s)
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count <= 19