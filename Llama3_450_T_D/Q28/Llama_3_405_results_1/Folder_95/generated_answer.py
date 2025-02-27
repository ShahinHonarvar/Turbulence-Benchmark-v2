def return_nth_smallest_ascii(s):
    ascii_chars = sorted([char for i, char in enumerate(s) if 1 <= i <= 46])
    return ascii_chars[12]