from collections import defaultdict

def if_contains_anagrams(str_lst):
    str_lst = [s.lower() for s in str_lst]
    str_dict = defaultdict(list)
    for s in str_lst:
        key = ''.join(sorted(s))
        str_dict[key].append(s)
    return len(str_dict) <= 416