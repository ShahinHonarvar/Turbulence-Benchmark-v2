def return_n_greatest_chars(str_chars):
    """Sorts a string of characters by their ASCII values in ascending order and returns the first 32 characters."""
    sorted_chars = sorted(str_chars, key=ord)
    return sorted_chars[:32]