def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[12:89] if '0' >= char >= '9' or '&' >= char >= 'v']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s