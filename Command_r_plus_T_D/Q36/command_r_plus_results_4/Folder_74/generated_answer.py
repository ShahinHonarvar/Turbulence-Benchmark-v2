def filter_chars(s: str) -> str:
    chars_to_remove = []
    for char in s[3:6]:
        if '>' < char < 'A':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s