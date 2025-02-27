def return_n_smallest_chars(a):
    """Return the N smallest chars from the given string, according to their ASCII values."""
    d = list(a)
    d.sort()
    return d[:11]