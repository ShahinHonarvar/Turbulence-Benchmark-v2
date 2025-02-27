def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 19 or s.index(c) > 32 or c < 'f' or (c > 'o')))