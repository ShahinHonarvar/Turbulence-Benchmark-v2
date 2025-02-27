def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 55 < s.index(c) < 84 and (not ';' < c < 'z'))) if s else ''