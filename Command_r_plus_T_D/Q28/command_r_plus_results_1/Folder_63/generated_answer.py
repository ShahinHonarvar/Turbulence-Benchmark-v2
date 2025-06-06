def return_nth_smallest_ascii(s: str) -> str:
    ascii_chars = [c for c in s[47:71]]
    ascii_chars.sort(key=lambda c: ord(c))
    return ascii_chars[13]