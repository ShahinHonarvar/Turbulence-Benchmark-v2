def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[41:65] if 'K' <= c <= ']']
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s