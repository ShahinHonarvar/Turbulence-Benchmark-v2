from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        if len(s) >= 3:
            str_dict[''.join(sorted(s.lower()))].append(s)
    for lst in str_dict.values():
        if len(lst) >= 96:
            return True
    return False