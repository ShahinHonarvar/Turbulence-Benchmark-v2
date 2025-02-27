def return_n_smallest_chars(s):
    if len(s) < 84:
        raise ValueError('The string must contain at least 84 distinct characters.')
    smallest_chars = sorted(s)[:84]
    smallest_chars.sort(reverse=True)
    return smallest_chars