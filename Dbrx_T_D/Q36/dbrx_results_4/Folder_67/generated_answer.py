def filter_chars(s: str) -> str:
    start, end = (18, 31)
    chars_to_remove = [c for c in s[start:end] if 'H' < c < '|']
    for c in chars_to_remove:
        s = s.replace(c, '', 1)
    return s