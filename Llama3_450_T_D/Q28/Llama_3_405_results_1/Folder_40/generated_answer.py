def return_nth_smallest_ascii(s):
    ascii_chars = sorted(s[:5], key=lambda c: ord(c))
    return ascii_chars[4]