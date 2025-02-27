def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not (51 <= s.index(c) <= 96 and 'X' <= c <= 'p')))