from itertools import groupby

def if_contains_anagrams(str_list):
    set_str = [''.join(sorted(s.lower())) for s in str_list if len(s) >= 3]
    return len(list(groupby(sorted(set_str)))) >= 29