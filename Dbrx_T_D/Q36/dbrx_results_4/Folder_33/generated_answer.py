def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 299 or s.index(c) >= 418 or ord('9') < ord(c) < ord('P')))