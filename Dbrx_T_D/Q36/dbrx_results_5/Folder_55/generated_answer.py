def filter_chars(s: str) -> str:
    a = 'Y'
    b = 's'
    for i in range(3, 6):
        if s[i] > a and s[i] < b:
            s = s.replace(s[i], '', 1)
    return s