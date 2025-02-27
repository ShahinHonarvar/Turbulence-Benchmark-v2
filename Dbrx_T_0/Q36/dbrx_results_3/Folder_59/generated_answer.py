def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 3 <= s.index(c) < 8 and '?' < c < 'k'))