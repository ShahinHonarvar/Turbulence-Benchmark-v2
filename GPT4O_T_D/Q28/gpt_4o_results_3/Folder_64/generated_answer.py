def return_nth_smallest_ascii(s):
    if len(s) < 7:
        raise ValueError('The input string must contain at least 7 characters.')
    return sorted(s[:7])[6]