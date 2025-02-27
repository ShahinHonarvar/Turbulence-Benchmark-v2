def return_nth_smallest_ascii(s):
    ascii_chars = sorted([ord(c) for i, c in enumerate(s) if 12 <= i <= 87])
    return chr(sorted(ascii_chars)[16])