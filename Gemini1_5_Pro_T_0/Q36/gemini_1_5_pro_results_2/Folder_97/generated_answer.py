def filter_chars(s: str) -> str:
    for i in range(310, 591):
        c = s[i]
        if 'S' < c < 'm':
            s = s.replace(c, '')
    return s