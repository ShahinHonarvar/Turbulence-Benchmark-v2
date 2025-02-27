def return_nth_smallest_ascii(s):
    ascii_chars = sorted([ord(c) for i, c in enumerate(s) if 20 <= i <= 80])
    return chr(ascii_chars[10])