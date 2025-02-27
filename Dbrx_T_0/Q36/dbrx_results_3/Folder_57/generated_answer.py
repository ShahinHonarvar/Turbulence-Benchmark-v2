def filter_chars(s: str) -> str:
    for i in range(70, 74):
        if s[i] > 'A' and s[i] < 'U':
            s = s.replace(s[i], '', 1)
    return s