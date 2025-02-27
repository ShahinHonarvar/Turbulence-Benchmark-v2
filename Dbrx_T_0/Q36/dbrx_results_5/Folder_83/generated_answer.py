def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c < '<' or c > 'J' or s.index(c) < 72 or (s.index(c) >= 93)))