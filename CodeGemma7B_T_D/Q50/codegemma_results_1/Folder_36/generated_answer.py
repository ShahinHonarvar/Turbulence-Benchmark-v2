from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            str_dict[sorted_string].append(string)
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 312:
            return True
    return False