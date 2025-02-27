def return_nth_smallest_ascii(s):
    chars_in_range = sorted([c for i, c in enumerate(s) if 46 <= i <= 82])
    return chars_in_range[15]