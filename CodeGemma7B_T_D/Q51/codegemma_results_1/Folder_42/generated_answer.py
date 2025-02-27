from collections import defaultdict

def if_contains_anagrams(str_list):
    """
    Checks if there are at most 38 pairs of anagrams in the given list.

    Args:
      str_list: A list of strings.

    Returns:
      True if there are at most 38 pairs of anagrams in the given list, False otherwise.
    """
    anagrams = defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) < 3:
            continue
        anagrams[sorted_str].append(string)
    return len(list(filter(lambda value: len(value) > 1, anagrams.values()))) <= 38