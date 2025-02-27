def return_nth_smallest_ascii(s):
    if len(s) < 6:
        raise ValueError('The input string must have at least 6 distinct characters.')
    return sorted(s[:6])[5]