def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 37 < ord(c) < 113 or 61 <= s.index(c) < 88))