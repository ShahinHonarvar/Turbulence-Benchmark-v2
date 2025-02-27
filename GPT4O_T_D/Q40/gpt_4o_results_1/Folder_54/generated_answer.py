def return_n_smallest_chars(s):
    if len(s) < 79:
        raise ValueError('String must contain at least 79 distinct characters.')
    smallest_chars = sorted(s)[:79]
    return sorted(smallest_chars, reverse=True)