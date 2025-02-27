def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[20:63] if 'i' <= char <= 'k']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s