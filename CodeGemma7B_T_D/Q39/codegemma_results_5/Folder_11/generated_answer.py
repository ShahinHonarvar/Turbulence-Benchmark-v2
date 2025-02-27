def return_n_greatest_chars(s):
    """Returns a sorted list of 17 characters from a string of distinct characters."""
    return sorted(s, key=ord)[-17:]