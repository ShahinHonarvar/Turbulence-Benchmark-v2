def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 43 < ord(c) < 108 or 44 <= s.index(c) <= 47))