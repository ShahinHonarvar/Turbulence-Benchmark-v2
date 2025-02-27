def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 63 < s.index(c) < 89 and '*' < c < 'w' or s.index(c) < 63 or s.index(c) >= 89))