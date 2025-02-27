def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not (49 < s.index(c) < 58 and 'I' < c < 'a'))) if s else ''