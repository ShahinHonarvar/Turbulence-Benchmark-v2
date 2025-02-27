def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c <= '?' or c >= 'm' or s.index(c) < 10 or (s.index(c) >= 79)))