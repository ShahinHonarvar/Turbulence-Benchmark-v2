def filter_chars(s: str) -> str:
    for i in range(1, 7):
        c = s[i]
        if '3' < c < '^':
            s = s.replace(c, '', 1)
    return s