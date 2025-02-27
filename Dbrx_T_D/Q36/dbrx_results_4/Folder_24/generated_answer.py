def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 10 or s.index(c) >= 15 or (c < 't' or c > 'v') for c in s))