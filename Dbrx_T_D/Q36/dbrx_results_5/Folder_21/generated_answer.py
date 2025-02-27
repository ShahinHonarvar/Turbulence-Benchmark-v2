def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c <= '*' or c >= '7' or 219 > s.index(c) > 403))