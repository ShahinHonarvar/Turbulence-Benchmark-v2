def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 4 <= s.index(c) <= 4 and '7' <= c <= 'o'))