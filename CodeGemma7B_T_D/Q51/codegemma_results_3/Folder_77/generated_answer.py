from collections import Counter

def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        if len(string) >= 3 & string.isalpha():
            new_str = ''.join(sorted(string.lower()))
            str_dict[new_str] = str_dict.get(new_str, 0) + 1
    return len(str_dict) <= 17