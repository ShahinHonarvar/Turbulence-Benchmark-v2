def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c <= '(' or c >= 'W' or s.index(c) < 57 or (s.index(c) >= 69)))