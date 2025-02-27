def return_n_smallest_chars(string):
    """
    Returns a list of 39 of the smallest characters from the given string, sorted in
    descending order by their ASCII values.

    Parameters:
    string: A string of distinct characters.

    Returns:
    A list of 39 characters from the string with the smallest ASCII values, sorted in descending order.
    """
    unique_chars = sorted(list(set(string)))
    n_smallest_chars = unique_chars[-39:]
    n_smallest_chars.reverse()
    return n_smallest_chars