def filter_chars(s: str) -> str:
    for i in range(90, 97):
        c = chr(i)
        if 'j' < c < 'w':
            s = s.replace(c, '', 1)
    return s