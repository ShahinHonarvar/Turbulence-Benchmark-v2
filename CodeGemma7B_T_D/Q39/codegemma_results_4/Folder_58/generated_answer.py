def return_n_greatest_chars(char_string):
    """Returns a sorted list of 49 characters from a string of distinct characters with the greatest ASCII values."""
    return sorted(char_string, key=ord, reverse=True)[:49]