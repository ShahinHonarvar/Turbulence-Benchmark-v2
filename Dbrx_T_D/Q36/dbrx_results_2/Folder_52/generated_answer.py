def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 73 < ord(c) < 97 or s.index(c) < 49 or s.index(c) >= 56))