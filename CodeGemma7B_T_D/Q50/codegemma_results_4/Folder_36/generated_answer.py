from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            str_dict[key].append(s)
    for v in str_dict.values():
        if len(v) >= 312:
            return True
    return False