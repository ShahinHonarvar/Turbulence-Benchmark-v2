def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c <= '(' or c >= ']' or s.index(c) < 163 or (s.index(c) >= 658)))