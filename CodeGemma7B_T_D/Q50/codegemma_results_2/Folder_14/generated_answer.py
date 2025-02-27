from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for string in str_list:
        string = string.lower().sort()
        anagram_dict[string].append(string)
    for anagram_group in anagram_dict.values():
        if len(anagram_group) >= 22:
            return True
    return False