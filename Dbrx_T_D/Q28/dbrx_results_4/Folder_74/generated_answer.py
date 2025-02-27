def return_nth_smallest_ascii(s):
    ascii_chars = [ord(c) for c in s if 1 <= ord(c) <= 31]
    ascii_chars.sort()
    return chr(ascii_chars[6]) if len(ascii_chars) > 6 else None