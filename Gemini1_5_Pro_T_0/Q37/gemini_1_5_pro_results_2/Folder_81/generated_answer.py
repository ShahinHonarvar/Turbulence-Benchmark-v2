def filter_chars(s: str) -> str:
    for i in range(19, 93):
        if i < len(s) and '8' <= s[i] <= 'm':
            c = s[i]
            s = s.replace(c, '')
    return s