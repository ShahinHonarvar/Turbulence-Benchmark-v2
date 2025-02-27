from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for word in str_list:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            str_dict[key].append(word)
    for group in str_dict.values():
        if len(group) >= 60:
            return True
    return False