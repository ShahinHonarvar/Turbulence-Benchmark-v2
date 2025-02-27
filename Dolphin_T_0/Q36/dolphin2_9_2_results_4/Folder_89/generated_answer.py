def filter_chars(s: str) -> str:
    for i in range(57, 69):
        if s[i] > '(' and s[i] < 'W':
            s = s.replace(s[i], '')
    return s