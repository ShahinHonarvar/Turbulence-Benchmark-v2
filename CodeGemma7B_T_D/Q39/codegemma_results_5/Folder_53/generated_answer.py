def return_n_greatest_chars(string):
    """
    Return the sorted list of the greatest ASCII values in a string.
    """
    return sorted(string, key=ord, reverse=True)[:19]