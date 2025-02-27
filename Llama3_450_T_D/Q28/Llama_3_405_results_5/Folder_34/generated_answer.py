def return_nth_smallest_ascii(s):
    ascii_chars = sorted([ord(c) for c in s[:19]])
    return chr(ascii_chars[18])