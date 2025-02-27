def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[27:30] if ';' <= c <= 'b']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s