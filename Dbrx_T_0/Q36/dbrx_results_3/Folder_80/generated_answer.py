def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 54 < s.index(c) < 92 and 'J' < c < 'X'))