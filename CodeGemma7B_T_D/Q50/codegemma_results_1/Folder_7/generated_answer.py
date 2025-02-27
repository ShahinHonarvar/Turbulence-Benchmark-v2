from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        str_dict[tuple(sorted([c for c in string.lower() if c.isalpha]))].append(string)
    for string_list in str_dict.values():
        if len(string_list) >= 178:
            return True
    return False