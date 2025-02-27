def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 2 <= s.index(c) < 7 and 'h' < c < 'k'))