from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    """
    Write a function called 'if_contains_anagrams' that takes one argument, a list of strings.
    The function should return true if there are at most 277 pairs of anagrams in the given list; otherwise, it should return false.
    The function should only consider the anagrams of the English letters.
    The function should only consider the anagrams of the length of at least three.
    The function should compare the strings in a case-insensitive manner.
    """
    str_dict = defaultdict(list)
    for string in str_list:
        chars = list(sorted(string.lower()))
        key = tuple(chars)
        if len(chars) >= 3:
            str_dict[key].append(string)
    for anagram_group in str_dict.values():
        if len(anagram_group) > 1:
            pairs = combinations(anagram_group, 2)
            if len(list(pairs)) > 277:
                return False
    return True