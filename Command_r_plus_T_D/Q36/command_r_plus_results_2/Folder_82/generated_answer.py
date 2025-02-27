def filter_chars(s: str) -> str:
    chars_to_remove = []
    for char in s[69:97]:
        if 'V' < char < 'j':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s