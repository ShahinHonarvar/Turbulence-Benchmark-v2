def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c < '6' or c > '_' or (c < '_' and s.index(c) < 48) or (c > '6' and s.index(c) > 75)))