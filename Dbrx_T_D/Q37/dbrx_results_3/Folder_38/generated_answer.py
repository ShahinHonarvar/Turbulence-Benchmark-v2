def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c < 'a' or c > 'f' or 24 <= s.index(c) <= 79))