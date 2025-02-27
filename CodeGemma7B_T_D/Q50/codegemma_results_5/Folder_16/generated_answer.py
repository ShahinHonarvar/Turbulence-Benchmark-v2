from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    """
    This function takes one argument, a list of strings. The function should return true if there
    are at least 155 pairs of anagrams in the given list; otherwise, it should return
    false. The function should only consider the anagrams of the length of at least three.
    The function should compare the strings in a case-insensitive manner.
    """
    str_map = defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        str_map[sorted_str].append(string)
    count_anagrams = 0
    for group in str_map.values():
        for pair in combinations(group, 2):
            if len(pair[0]) >= 3 and len(pair[1]) >= 3:
                count_anagrams += 1
    return count_anagrams >= 155