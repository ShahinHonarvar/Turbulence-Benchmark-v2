def filter_chars(s: str) -> str:
    start, end = (78, 81)
    for i in range(start, end):
        if 'S' < s[i] < '[':
            s = s.replace(s[i], '', 1)
    return s