def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 52 or s.index(c) > 88 or (c < 'c' and c > '&')))