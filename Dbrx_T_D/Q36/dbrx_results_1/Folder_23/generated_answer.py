def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 21 or i > 25 or (not '5' < c < '}')))