def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not ('&' < c < 'c' and 52 < s.index(c) < 88)))