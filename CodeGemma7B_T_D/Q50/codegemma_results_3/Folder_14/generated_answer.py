from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            str_dict[sorted_str].append(string)
    for lst in str_dict.values():
        if len(lst) >= 22:
            return True
    return False