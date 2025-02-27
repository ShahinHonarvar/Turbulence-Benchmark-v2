def return_nth_smallest_ascii(s):
    ascii_chars = sorted([char for i, char in enumerate(s) if i <= 18])
    return ascii_chars[12]