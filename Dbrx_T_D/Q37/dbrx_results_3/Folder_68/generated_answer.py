def filter_chars(s: str) -> str:
    for i in range(7, 10):
        char = s[i]
        if '6' <= char <= 'w':
            s = s.replace(char, '', 1)
    return s