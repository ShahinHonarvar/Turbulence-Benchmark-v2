def return_nth_smallest_ascii(s):
    if len(s) < 80:
        raise ValueError('The string must have at least 80 characters.')
    sub_str = s[52:80]
    sorted_chars = sorted(sub_str)
    return sorted_chars[6]