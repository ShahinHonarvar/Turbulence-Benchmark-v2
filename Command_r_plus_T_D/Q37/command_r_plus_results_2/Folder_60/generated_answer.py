def filter_chars(s: str) -> str:
    chars_to_remove = []
    for i, char in enumerate(s[12:78], 12):
        if ':' <= char <= 'L':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s