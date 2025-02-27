def return_nth_smallest_ascii(s):
    ascii_chars = sorted([c for i, c in enumerate(s) if 17 <= i <= 83], key=lambda x: ord(x))
    return ascii_chars[4]