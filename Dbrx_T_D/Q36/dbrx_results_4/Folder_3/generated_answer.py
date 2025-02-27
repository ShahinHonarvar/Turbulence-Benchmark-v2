def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c <= '!' or c >= '?' or s[41:78].find(c) == -1))