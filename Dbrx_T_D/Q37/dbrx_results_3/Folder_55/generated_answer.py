def filter_chars(s: str) -> str:
    chars_to_remove = set(s[1:6])[ord('$'):ord(';') + 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s