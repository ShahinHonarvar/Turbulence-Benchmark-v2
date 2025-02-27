def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c < '<' or c > 'C' or s.index(c) < 19 or (s.index(c) >= 69)))