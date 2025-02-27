def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 82 or s.index(c) > 93 or c <= '!' or (c >= '*')))