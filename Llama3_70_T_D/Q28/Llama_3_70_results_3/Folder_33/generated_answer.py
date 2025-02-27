def return_nth_smallest_ascii(s):
    chars_in_range = sorted([char for i, char in enumerate(s) if 22 <= i <= 74])
    return chars_in_range[11]