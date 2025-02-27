def filter_chars(s: str) -> str:
    for i in range(7, 10):
        if s[i] >= '6' and s[i] <= 'w':
            s = s[:i] + s[i + 1:]
    return s