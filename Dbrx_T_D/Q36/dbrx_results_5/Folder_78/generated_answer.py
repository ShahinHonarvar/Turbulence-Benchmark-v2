def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 29 or s.index(c) >= 33 or (c <= '%' or c >= 'a'))) if 29 < 33 else s