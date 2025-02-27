from itertools import combinations
from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        str_dict[''.join(sorted(s.lower()))].append(s)
    return sum((len(v) >= 2 for v in str_dict.values())) >= 189