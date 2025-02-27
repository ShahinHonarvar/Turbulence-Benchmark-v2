from collections import defaultdict

def if_contains_anagrams(str_list):
    """
    This function checks if there are at most 392 pairs of anagrams in the given list.

    Args:
    str_list: A list of strings.

    Returns:
    True if there are at most 392 pairs of anagrams, False otherwise.
    """
    str_dict = defaultdict(list)
    for string in str_list:
        hashed_string = ''.join(sorted(string.lower()))
        str_dict[hashed_string].append(string)
    count = 0
    for group in str_dict.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 392