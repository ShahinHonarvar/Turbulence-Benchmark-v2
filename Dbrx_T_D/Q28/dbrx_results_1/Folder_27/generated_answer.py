def return_nth_smallest_ascii(s):
    ascii_chars = [ord(c) for c in s if 33 <= ord(c) <= 85]
    ascii_chars.sort()
    return chr(ascii_chars[12])