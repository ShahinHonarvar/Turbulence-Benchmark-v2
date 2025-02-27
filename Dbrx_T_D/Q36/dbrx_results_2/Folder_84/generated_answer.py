def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 171 or i > 636 or (c > 'c' and c < 's') or (s.index(c, i + 1) == -1)))