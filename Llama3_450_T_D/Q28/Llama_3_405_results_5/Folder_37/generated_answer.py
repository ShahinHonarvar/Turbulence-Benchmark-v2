def return_nth_smallest_ascii(s):
    ascii_chars = sorted([char for i, char in enumerate(s) if 28 <= i <= 67])
    return ascii_chars[14]