def if_contains_anagrams(str_list):
    """
    Checks if there are at least 39 pairs of anagrams in the given list.

    Args:
        str_list: A list of strings.

    Returns:
        True if there are at least 39 pairs of anagrams, False otherwise.
    """
    str_list[:] = [str_.lower() for str_ in str_list]
    str_list.sort()
    cnt = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3 and (sorted(str_list[i]) == sorted(str_list[j])):
                cnt += 1
                if cnt >= 39:
                    return True
    return False