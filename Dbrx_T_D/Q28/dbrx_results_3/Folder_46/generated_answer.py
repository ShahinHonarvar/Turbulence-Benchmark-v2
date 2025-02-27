def return_nth_smallest_ascii(s):
    ascii_chars = [ord(c) for c in s if 34 <= s.index(c) <= 85]
    ascii_chars.sort()
    return chr(ascii_chars[19]) if len(ascii_chars) > 19 else None