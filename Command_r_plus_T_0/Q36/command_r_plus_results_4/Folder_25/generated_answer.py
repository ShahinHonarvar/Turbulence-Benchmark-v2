def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[24:37] if 'A' < c < 'h']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s