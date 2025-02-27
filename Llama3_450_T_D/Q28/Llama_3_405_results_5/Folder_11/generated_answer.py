def return_nth_smallest_ascii(s):
    ascii_chars = sorted([c for i, c in enumerate(s) if 9 <= i <= 59], key=lambda x: ord(x))
    return ascii_chars[5]