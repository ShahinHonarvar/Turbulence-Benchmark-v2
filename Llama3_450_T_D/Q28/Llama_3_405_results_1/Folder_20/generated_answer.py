def return_nth_smallest_ascii(s):
    ascii_chars = sorted([ord(c) for i, c in enumerate(s) if 25 <= i <= 64])
    return chr(ascii_chars[5])