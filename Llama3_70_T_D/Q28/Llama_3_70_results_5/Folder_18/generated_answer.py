def return_nth_smallest_ascii(s):
    chars_in_range = sorted([s[i] for i in range(51, 61)])
    return chars_in_range[4]