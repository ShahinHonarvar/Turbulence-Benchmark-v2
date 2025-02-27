def filter_chars(s: str) -> str:
    chars_to_remove = []
    for char in s[5:6]:
        if 'I' < char < 'a':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s