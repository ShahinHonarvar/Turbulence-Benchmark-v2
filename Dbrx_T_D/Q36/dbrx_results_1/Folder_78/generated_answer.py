def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[29:33] if ord('%') < ord(c) < ord('a')]
    for c in chars_to_remove:
        s = s.replace(c, '', 1)
    return s