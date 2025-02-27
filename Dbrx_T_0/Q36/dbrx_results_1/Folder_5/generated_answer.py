def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 55 < s.index(c) < 66 and (not 'f' < c < '|'))) if s else ''