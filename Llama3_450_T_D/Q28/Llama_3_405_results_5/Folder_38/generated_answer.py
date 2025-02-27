def return_nth_smallest_ascii(s):
    ascii_chars = sorted([ord(c) for i, c in enumerate(s) if i <= 45])
    return chr(ascii_chars[9])