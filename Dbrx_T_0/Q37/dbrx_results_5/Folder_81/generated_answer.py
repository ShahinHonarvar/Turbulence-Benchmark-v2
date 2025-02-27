def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 19 <= s.index(c) <= 92 and '8' <= c <= 'm'))