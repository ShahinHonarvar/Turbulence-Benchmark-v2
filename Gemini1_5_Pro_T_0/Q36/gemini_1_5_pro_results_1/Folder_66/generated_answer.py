def filter_chars(s: str) -> str:
    for i in range(39, 87):
        if s[i] > '!' and s[i] < '}':
            s = s.replace(s[i], '')
    return s