from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for s in string_list:
        sorted_s = ''.join(sorted(filter(str.isalpha, s.lower())))
        if len(sorted_s) >= 3:
            anagram_dict[sorted_s].append(s)
    for anagram_group in anagram_dict.values():
        if len(anagram_group) > 1:
            anagram_count += len(anagram_group) * (len(anagram_group) - 1) // 2
            if anagram_count > 79:
                return False
    return True