def return_n_greatest_chars(char_string):
    """Given a string of distinct characters, return a list of the greatest 57 characters with the greatest ASCII values."""
    return sorted(char_string)[-57:]