from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            str_dict[sorted_s].append(s)
    return len(str_dict) >= 28