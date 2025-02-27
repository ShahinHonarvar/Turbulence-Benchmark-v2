def filter_chars(s: str) -> str:
    start, end = (29, 33)
    for i in range(start, end):
        if '%' < s[i] < 'a':
            s = s.replace(s[i], '', 1)
    return s