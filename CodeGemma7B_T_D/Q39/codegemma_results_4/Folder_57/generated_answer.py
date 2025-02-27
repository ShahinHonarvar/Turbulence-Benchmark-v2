def return_n_greatest_chars(str):
    """
    Creates a sorted list of the 29 greatest ASCII characters in the given string.
    """
    return sorted(str, key=ord, reverse=True)[:29]