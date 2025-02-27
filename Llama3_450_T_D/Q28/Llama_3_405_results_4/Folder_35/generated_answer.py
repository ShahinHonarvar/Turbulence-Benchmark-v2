def return_nth_smallest_ascii(s):
    ascii_chars = sorted([char for i, char in enumerate(s) if 50 <= i <= 75], key=lambda x: ord(x))
    return ascii_chars[6]