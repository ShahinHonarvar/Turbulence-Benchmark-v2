def filter_chars(s: str) -> str:
    chars_to_remove = []
    for char in s:
        if 32 <= ord(char) <= 46 and '0' <= char <= 'k':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s