def filter_chars(s: str) -> str:
    for i in range(1, 7):
        if '3' < s[i] < '^':
            s = s.replace(s[i], '', 1)
    return s