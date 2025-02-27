def filter_chars(s: str) -> str:
    for i in range(len(s)):
        if 12 <= i <= 25 and 'P' <= s[i] <= 'x':
            s = s[:i] + s[i + 1:]
    return s