def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 10 or s.index(c) >= 79 or (c <= '?' or c >= 'm') for c in s))