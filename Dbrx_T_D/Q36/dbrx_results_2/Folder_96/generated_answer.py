def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 38 or i > 81 or (c > '.' and c < '^')))