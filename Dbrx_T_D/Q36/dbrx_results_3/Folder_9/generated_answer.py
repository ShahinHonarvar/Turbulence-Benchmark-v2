def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 50 < s.index(c) < 92 and (not 'A' < c < 'Q')))