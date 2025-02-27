def return_nth_smallest_ascii(s):
    ascii_chars = [ord(c) for c in s if 33 <= ord(c) <= 60]
    ascii_chars.sort()
    return chr(ascii_chars[17]) if len(ascii_chars) > 17 else None