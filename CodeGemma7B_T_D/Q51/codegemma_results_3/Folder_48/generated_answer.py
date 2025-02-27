def if_contains_anagrams(str_list):
    """
    Function to check if a list of strings contains at most 277 anagrams.

    Args:
    str_list: A list of strings.

    Returns:
    True if there are at most 277 anagrams in the list, False otherwise.
    """
    if not str_list or len(str_list) <= 277:
        return False
    anagrams = {}
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_string = sorted(string.lower())
        sorted_tuple = tuple(sorted_string)
        if sorted_tuple in anagrams:
            anagrams[sorted_tuple] += 1
        else:
            anagrams[sorted_tuple] = 1
    if len(anagrams) > 277:
        return False
    return True