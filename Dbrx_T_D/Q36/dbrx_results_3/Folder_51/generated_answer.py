def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 58 <= s.index(c) < 58 + 24 or s.index(c) < 58 or s.index(c) >= 81 or (not '5' < c < '>')))