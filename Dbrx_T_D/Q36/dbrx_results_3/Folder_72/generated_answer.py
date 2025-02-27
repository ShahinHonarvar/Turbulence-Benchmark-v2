def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c < 'W' or c > 'x' or s.index(c) < 44 or (s.index(c) >= 68)))