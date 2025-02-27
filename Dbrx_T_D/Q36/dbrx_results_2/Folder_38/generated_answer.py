def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not (44 < s.index(c) < 48 and '+' < c < 'l') or s.index(c) < 44 or s.index(c) >= 48))