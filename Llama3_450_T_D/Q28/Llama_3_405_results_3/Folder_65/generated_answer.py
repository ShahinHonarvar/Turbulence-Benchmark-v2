def return_nth_smallest_ascii(s):
    ascii_chars = sorted([c for i, c in enumerate(s) if 32 <= i <= 67], key=lambda c: ord(c))
    return ascii_chars[11]