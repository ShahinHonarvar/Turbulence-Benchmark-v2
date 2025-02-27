def return_nth_smallest_ascii(s):
    if len(s) < 15:
        raise ValueError('String must have at least 15 characters.')
    return sorted(s[:15])[14]