def return_n_greatest_chars(str):
    """Return the n greatest characters in a string."""
    return sorted(str, key=ord, reverse=True)[:55]