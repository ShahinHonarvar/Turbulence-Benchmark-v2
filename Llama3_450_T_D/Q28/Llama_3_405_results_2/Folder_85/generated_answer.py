def return_nth_smallest_ascii(s):
    ascii_chars = sorted([ord(c) for i, c in enumerate(s) if 17 <= i <= 86])
    return chr(ascii_chars[14])