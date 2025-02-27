def return_n_smallest_chars(string):
    """Return the N smallest chars of a given string."""
    return sorted(string, key=ord, reverse=True)[:49]