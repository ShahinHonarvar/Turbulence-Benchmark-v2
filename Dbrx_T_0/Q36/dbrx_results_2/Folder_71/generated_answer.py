def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 82 or s.index(c) >= 89 or (not '*' < c < '[')))