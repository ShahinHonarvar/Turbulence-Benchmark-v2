def filter_chars(s: str) -> str:
    for i in range(len(s)):
        if 7 <= i <= 8 and 'B' <= s[i] <= 'H':
            s = s[:i] + s[i + 1:]
    return s