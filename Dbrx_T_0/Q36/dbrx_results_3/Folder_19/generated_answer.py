def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c <= ';' or c >= 'r' or s.index(c) < 77 or (s.index(c) >= 87)))