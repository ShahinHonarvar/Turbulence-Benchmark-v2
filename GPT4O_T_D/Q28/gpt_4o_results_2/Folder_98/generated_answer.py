def return_nth_smallest_ascii(s):
    if len(s) < 9:
        raise ValueError('String must have at least 9 characters.')
    return sorted(s[:9])[8]