def filter_chars(s: str) -> str:
    for i in range(3, 5):
        if 'Y' < s[i] < 's':
            s = s.replace(s[i], '', 1)
    return s