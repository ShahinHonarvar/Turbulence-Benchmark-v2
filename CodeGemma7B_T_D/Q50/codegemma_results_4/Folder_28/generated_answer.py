from itertools import combinations

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = sorted(str_list, key=len)
    str_list = [s for s in str_list if len(s) >= 3]
    str_dict = {}
    for str in str_list:
        sorted_str = ''.join(sorted(str))
        str_dict.setdefault(sorted_str, []).append(str)
    for key in str_dict.values():
        if len(key) >= 81:
            return True
    return False