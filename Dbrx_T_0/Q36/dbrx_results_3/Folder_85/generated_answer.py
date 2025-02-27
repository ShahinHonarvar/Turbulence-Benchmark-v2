def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 55 <= s.index(c) < 80 and (not 'S' < c < 's'))) if s else ''