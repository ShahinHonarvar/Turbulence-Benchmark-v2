from collections import defaultdict

def if_contains_anagrams(str_list):
    """
    Checks if a list of strings contains at most 206 pairs of anagrams.

    Args:
      str_list: A list of strings.

    Returns:
      True if the list contains at most 206 pairs of anagrams, False otherwise.
    """
    anagram_counts = defaultdict(int)
    for string in str_list:
        sorted_string = sorted(string.lower())
        if sorted_string in anagram_counts:
            anagram_counts[sorted_string] += 1
        else:
            anagram_counts[sorted_string] = 1
    if len(anagram_counts) > 206:
        return False
    return True