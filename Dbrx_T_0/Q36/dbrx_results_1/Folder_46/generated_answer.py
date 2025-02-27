def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 19 < s.index(c) < 69 and (not '<' < c < 'C'))) if s else ''