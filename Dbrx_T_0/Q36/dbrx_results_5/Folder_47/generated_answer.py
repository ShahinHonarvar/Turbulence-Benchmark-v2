def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 45 < s.index(c) < 57 and ord('F') < ord(c) < ord('n') or s.index(c) <= 45 or s.index(c) >= 57))