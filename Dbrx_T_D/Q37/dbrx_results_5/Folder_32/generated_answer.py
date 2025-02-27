def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[23:90] if 'w' <= c <= '{']
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s