def return_n_smallest_chars(s):
    """
    Returns a list of exactly 6 characters of the given string that have the smallest ASCII values.

    Args:
        s: A string of distinct characters.

    Returns:
        A sorted list of 6 characters with the smallest ASCII values.
    """
    return sorted(s, key=ord, reverse=True)[:6]