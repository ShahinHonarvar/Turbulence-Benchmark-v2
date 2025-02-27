def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 43 < ord(c) < 83 or s.index(c) < 43 or s.index(c) >= 83))