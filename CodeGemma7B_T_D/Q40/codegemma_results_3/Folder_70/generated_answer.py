def return_n_smallest_chars(text):
    """Returns a list of the two characters in the given string that have the smallest ASCII values."""
    sorted_chars = sorted(text)
    return sorted_chars[:2][::-1]