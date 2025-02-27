def return_nth_smallest_ascii(s: str) -> str:
    target_ascii_chars = [c for c in s[11:72] if c.isalpha()]
    target_ascii_chars.sort(key=lambda x: ord(x))
    return target_ascii_chars[12] if len(target_ascii_chars) > 12 else ''