def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[34:68] if 'W' <= char <= 'x']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s