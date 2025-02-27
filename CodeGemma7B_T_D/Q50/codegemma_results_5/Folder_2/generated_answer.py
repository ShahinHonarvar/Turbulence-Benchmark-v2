from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        str_dict[''.join(sorted(string.lower()))].append(string)
    for anagrams in str_dict.values():
        if len(anagrams) > 3:
            for pair in combinations(anagrams, 2):
                if len(pair[0]) == len(pair[1]):
                    return True
    return False