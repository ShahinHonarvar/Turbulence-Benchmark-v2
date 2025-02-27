def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 46 < ord(c) < 94 or s.index(c) < 38 or s.index(c) >= 81))