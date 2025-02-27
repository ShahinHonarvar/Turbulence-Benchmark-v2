import functools

def return_n_greatest_chars(str_dist_chars):
    """Returns the sorted list of 46 characters of the given string with greatest ASCII values."""
    return functools.reduce(lambda result, ch: sorted(result + [ch], key=ord)[-46:], str_dist_chars, [])