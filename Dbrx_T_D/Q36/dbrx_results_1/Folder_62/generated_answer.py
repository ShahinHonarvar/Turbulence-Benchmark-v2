def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 63 or s.index(c) >= 89 or c <= '*' or (c >= 'w')))