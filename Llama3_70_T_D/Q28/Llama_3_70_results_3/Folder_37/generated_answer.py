def return_nth_smallest_ascii(s):
    chars_in_range = [c for i, c in enumerate(s) if 28 <= i <= 67]
    unique_chars_in_range = sorted(set(chars_in_range))
    return unique_chars_in_range[14]