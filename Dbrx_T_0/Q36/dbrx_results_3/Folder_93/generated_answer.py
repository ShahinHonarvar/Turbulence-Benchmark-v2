def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 52 > s.index(c) >= 88 or not '&' < c < 'c'))