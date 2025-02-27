def return_nth_smallest_ascii(s):
    chars_in_range = sorted(s[34:86])
    return chars_in_range[19] if len(chars_in_range) > 20 else None