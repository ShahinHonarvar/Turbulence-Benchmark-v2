def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not ('&' < c < 'M' and 46 < s.index(c) < 74)))