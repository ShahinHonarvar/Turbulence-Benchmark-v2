def return_nth_smallest_ascii(s: str) -> str:
    ascii_chars = [c for c in s[33:61] if 33 <= ord(c) <= 60]
    ascii_chars.sort(key=ord)
    return ascii_chars[17] if len(ascii_chars) > 18 else ''