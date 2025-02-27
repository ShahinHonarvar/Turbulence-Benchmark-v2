def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 23 <= s.index(c) < 83 or c <= 'f' or c >= 'o'))