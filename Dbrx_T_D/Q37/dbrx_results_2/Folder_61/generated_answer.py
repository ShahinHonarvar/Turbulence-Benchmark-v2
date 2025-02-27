def filter_chars(s: str) -> str:
    for i in range(len(s)):
        if 5 <= i <= 6 and 'G' <= s[i] <= 'p':
            s = s[:i] + s[i + 1:]
    return s