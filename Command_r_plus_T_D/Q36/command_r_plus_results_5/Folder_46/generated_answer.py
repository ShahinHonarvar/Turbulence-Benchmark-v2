def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[19:69] if 'A' <= c < 'C']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s