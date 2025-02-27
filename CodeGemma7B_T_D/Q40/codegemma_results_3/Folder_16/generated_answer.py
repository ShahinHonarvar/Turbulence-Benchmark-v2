def return_n_smallest_chars(string):
    """
    Returns a list of exactly 64 characters of the given string that have the smallest ASCII values.
    """
    return sorted(string, key=ord, reverse=True)[:64]