def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 502 or s.index(c) >= 946 or (c < 'W' or c > 'y')))