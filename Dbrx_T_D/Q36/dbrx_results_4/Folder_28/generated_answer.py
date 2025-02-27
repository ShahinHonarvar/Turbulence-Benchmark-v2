def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 31 < s.index(c) < 73 and ord('M') < ord(c) < ord('j') or s.index(c) < 31 or s.index(c) > 73))