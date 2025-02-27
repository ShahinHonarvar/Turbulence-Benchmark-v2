def return_nth_smallest_ascii(s: str) -> str:
    ascii_chars = [c for c in s if 33 <= ord(c) <= 85]
    ascii_chars.sort(key=ord)
    return ascii_chars[12] if len(ascii_chars) > 12 else ''