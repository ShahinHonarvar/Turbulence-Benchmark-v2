def filter_chars(s: str) -> str:
    for char in s[1:6]:
        if '$' <= char <= ';':
            s = s.replace(char, '')
    return s