def return_n_greatest_chars(s):
    """Return sorted list of two characters with greatest ASCII values in a string."""
    return sorted(s, key=ord, reverse=True)[:2]