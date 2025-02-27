def filter_chars(s: str) -> str:
    for char in s[69:81]:
        if '@' <= char <= 'p':
            s = s.replace(char, '')
    return s