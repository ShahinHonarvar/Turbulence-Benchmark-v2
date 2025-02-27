def return_nth_smallest_ascii(s):
    ascii_chars = [ord(c) for c in s if 25 <= s.index(c) <= 64]
    ascii_chars.sort()
    return chr(ascii_chars[5]) if ascii_chars else None