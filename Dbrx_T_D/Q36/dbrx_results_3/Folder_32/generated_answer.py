def filter_chars(s: str) -> str:
    for i in range(min(63, len(s)), max(40, 0), -1):
        char = s[i]
        if '7' < char < 'H':
            s = s[:i] + s[i + 1:]
    return s