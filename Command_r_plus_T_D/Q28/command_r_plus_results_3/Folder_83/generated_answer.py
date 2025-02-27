def return_nth_smallest_ascii(s: str) -> str:
    ascii_chars = [c for c in s[30:71] if c.isalpha()]
    ascii_chars.sort(key=lambda x: ord(x))
    return ascii_chars[14] if len(ascii_chars) > 15 else ''