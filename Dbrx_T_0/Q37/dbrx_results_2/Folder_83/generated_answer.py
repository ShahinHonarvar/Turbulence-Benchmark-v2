def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 29 <= s.index(c) <= 79 and 'K' <= c <= 'z' or s.index(c) < 29 or s.index(c) > 79))