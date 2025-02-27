def filter_chars(s: str) -> str:
    start, end = (18, 38)
    chars_to_remove = [c for c in s[start:end] if ord(')') < ord(c) < ord('P')]
    for c in chars_to_remove:
        s = s.replace(c, '', 1)
    return s