def if_contains_anagrams(str_list):
    """
    Checks if there are at most 445 pairs of anagrams in a list of strings.

    Args:
        str_list: A list of strings.

    Returns:
        True if there are at most 445 pairs of anagrams, False otherwise.
    """
    str_list = [''.join((c for c in s if c.isalpha())) for s in str_list]
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    num_pairs = 0
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]):
                num_pairs += 1
                if num_pairs > 445:
                    return False
    return True