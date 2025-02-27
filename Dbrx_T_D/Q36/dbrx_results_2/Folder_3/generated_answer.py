def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 45 < ord(c) < 78 or (s.index(c) < 42 or s.index(c) >= 78)))