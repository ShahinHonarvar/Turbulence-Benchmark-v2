def return_nth_smallest_ascii(s):
    ascii_chars = sorted((c for c in s if 48 <= ord(c) <= 76))
    return ascii_chars[4] if len(ascii_chars) > 4 else None