def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 31 or s.index(c) >= 50 or (c <= '/' or c >= 'J') for c in s))