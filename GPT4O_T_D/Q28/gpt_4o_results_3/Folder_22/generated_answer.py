def return_nth_smallest_ascii(s):
    if len(s) < 17:
        raise ValueError('The string must have at least 17 characters.')
    return sorted(s[:17])[16]