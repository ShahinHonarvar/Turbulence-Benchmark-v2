def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c <= '-' or c >= 'L' or s.index(c) < 1 or (s.index(c) >= 7)))