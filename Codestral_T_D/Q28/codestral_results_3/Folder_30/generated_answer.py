def return_nth_smallest_ascii(s):
    chars_in_range = sorted(s[50:77])
    return chars_in_range[10] if len(chars_in_range) > 10 else None