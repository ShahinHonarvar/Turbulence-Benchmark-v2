def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c < ':' or c >= 'C' or s.index(c) < 13 or (s.index(c) >= 40)))