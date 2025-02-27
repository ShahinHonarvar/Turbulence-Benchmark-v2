def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 59 < ord(c) < 114 or s.index(c) < 77 or s.index(c) >= 87))