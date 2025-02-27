def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 42 < s.index(c) < 68 and (not 't' < c < 'x')))