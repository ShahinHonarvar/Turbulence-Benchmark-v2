def return_nth_smallest_ascii(s):
    if len(s) < 56:
        raise ValueError('String must be at least 56 characters long.')
    subset = s[12:56]
    sorted_chars = sorted(subset, key=lambda x: ord(x))
    if len(sorted_chars) < 17:
        raise ValueError('The substring does not contain 17 distinct characters.')
    return sorted_chars[16]