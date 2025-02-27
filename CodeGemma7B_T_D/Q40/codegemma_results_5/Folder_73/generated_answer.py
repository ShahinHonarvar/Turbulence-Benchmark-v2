def return_n_smallest_chars(distinct_chars):
    """
    Returns a list of 80 characters from the given string with the smallest ASCII values.
    """
    char_list = list(distinct_chars)
    char_list.sort()
    return char_list[:80]