def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 44 <= s.index(c) < 68 and (not 'W' < c < 'x'))) if s else ''