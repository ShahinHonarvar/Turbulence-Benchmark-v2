def return_n_smallest_chars(s):
    if len(s) < 27:
        raise ValueError('Input string must have at least 27 distinct characters.')
    smallest_chars = sorted(s)[:27]
    return sorted(smallest_chars, reverse=True)