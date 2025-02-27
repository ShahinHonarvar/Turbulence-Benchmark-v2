from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    """
    This function checks if there are at most 59 pairs of anagrams in the given list.

    Args:
        str_list: A list of strings.

    Returns:
        True if there are at most 59 pairs of anagrams, False otherwise.
    """
    anagrams = defaultdict(list)
    for string in str_list:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    lengths = [len(anagram_list) for anagram_list in anagrams.values()]
    lengths.sort(reverse=True)
    num_pairs = sum((L * (L - 1) // 2 for L in lengths))
    return num_pairs <= 59