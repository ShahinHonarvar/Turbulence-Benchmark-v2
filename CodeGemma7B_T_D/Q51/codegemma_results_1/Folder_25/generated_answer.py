from collections import defaultdict

def if_contains_anagrams(str_list):
    """
    Checks if a list of strings contains at most 67 anagrams.

    Args:
        str_list: A list of strings.

    Returns:
        True if there are at most 67 pairs of anagrams, False otherwise.
    """
    anagrams = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in anagrams:
            anagrams[sorted_string].append(string)
    return len(anagrams) <= 67