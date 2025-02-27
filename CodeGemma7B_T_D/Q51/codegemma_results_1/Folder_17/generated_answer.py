from collections import defaultdict

def if_contains_anagrams(str_list):
    """
    Checks if the given list of strings contains anagrams in at most 22 pairs.

    Args:
        str_list: A list of strings.

    Returns:
        True if there are at most 22 pairs of anagrams in the given list; otherwise, False.
    """
    str_dict = defaultdict(list)
    for string in str_list:
        string = ''.join(sorted(string.lower()))
        str_dict[string].append(string)
    num_pairs = 0
    for anagrams in str_dict.values():
        if len(anagrams) > 1:
            num_pairs += len(anagrams) // 2
    return num_pairs <= 22