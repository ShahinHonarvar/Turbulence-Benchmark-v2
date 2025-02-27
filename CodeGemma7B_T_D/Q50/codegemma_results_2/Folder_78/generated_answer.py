from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    """
    Returns True if there are at least 79 pairs of anagrams in the list, False otherwise.
    The function considers anagrams with a length of at least three characters and compares them case-insensitively.
    """
    char_to_strings = defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        char_to_strings[sorted_str].append(string)
    num_anagrams = 0
    for anagram_list in char_to_strings.values():
        for pair in combinations(anagram_list, 2):
            if len(pair[0]) >= 3 and len(pair[1]) >= 3:
                num_anagrams += 1
    return num_anagrams >= 79