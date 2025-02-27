def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c < 'W' or c > 'y' or s.index(c) < 502 or (s.index(c) >= 946)))