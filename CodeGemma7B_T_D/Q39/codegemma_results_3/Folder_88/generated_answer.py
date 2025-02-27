def return_n_greatest_chars(string):
    """
    Returns the sorted list of exactly 84 characters of the given string
    that have the greatest ASCII values. The function sorts the list
    in ascending order and returns it.
    """
    chars = list(string)
    chars.sort(reverse=True)
    return chars[:84]