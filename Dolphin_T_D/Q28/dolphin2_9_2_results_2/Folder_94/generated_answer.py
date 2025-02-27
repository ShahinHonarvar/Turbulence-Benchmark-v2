def return_nth_smallest_ascii(s):
    chars = s[6:59]
    ascii_chars = [ord(c) for c in chars]
    ascii_chars.sort()
    return chr(ascii_chars[18])