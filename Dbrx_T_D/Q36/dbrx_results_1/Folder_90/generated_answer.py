def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 344 or s.index(c) > 874 or c < 'f' or (c > '~')))