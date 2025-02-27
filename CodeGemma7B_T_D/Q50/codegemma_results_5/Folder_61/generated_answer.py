from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        sorted_s = ''.join(sorted(s))
        str_dict[sorted_s].append(s)
    pairs = []
    for anagrams in str_dict.values():
        if len(anagrams) >= 3:
            pairs.extend(combinations(anagrams, 2))
    return len(pairs) >= 8