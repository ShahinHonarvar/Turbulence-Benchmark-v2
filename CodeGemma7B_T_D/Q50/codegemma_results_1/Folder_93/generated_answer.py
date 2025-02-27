from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        sorted_str = tuple(sorted(string.lower()))
        str_dict[sorted_str].append(string)
    for value_list in str_dict.values():
        if len(value_list) >= 18:
            return True
    return False