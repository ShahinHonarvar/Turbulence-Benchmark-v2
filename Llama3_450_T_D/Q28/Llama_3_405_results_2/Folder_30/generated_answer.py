def return_nth_smallest_ascii(s):
    ascii_chars = sorted([ord(c) for i, c in enumerate(s) if 50 <= i <= 76])
    return chr(sorted(ascii_chars)[10])