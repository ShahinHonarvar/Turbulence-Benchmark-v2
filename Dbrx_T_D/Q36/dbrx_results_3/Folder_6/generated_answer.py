def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 31 or s.index(c) > 70 or (c < 'B' or c > 'v')))