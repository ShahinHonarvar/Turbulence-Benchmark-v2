def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not 44 < s.index(c) < 68 or not 'W' < c < 'x'))