def return_n_smallest_chars(s):
    if len(s) < 68:
        raise ValueError('The string must contain at least 68 distinct characters.')
    return sorted(s)[:68]