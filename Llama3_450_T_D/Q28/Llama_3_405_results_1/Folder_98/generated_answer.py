def return_nth_smallest_ascii(s):
    ascii_chars = sorted([ord(c) for i, c in enumerate(s) if i <= 8])
    return chr(ascii_chars[8])