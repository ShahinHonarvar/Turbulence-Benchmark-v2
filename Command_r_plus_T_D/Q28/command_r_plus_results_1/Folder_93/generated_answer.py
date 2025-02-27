def return_nth_smallest_ascii(s: str) -> str:
    ascii_chars = [c for c in s[42:60]]
    ascii_chars.sort(key=lambda x: ord(x))
    return ascii_chars[16]