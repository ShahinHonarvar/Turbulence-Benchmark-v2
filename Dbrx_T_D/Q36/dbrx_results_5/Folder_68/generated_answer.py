def filter_chars(s: str) -> str:
    for i in range(1, 10, 1):
        if '8' < s[i] < 'm':
            s = s.replace(s[i], '', 1)
    return s