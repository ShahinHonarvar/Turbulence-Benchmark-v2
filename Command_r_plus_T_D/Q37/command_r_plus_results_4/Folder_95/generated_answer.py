def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[35:41] if ')' <= char <= 'l']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s