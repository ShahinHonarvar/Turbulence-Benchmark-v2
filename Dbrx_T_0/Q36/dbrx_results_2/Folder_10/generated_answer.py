def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 35 <= s.index(c) < 60 and (not '!' < c < 'B')))