def filter_chars(s: str) -> str:
    for i in range(min(70, len(s)), max(61, len(s))):
        if '0' <= s[i] <= '@':
            s = s[:i] + s[i + 1:]
    return s