from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for str in str_list:
        str_dict[''.join(sorted(str.lower()))].append(str)
    for sublist in str_dict.values():
        if len(sublist) >= 35:
            return True
    return False