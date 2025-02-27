def return_nth_smallest_ascii(s):
    ascii_chars = sorted(s[:8], key=lambda x: ord(x))
    return ascii_chars[7]