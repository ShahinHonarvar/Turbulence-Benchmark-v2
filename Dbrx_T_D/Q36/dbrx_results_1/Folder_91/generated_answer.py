def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 0 or s.index(c) > 3 or ord('$') < ord(c) < ord('?'))).strip()