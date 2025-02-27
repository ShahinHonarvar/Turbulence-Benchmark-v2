def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not ('?' < c < 'k' and 3 <= s.index(c) < 8)))