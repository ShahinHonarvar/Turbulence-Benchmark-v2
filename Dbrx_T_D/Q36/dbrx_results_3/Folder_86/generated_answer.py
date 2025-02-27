def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 672 or i >= 709 or (not 'X' < c < '}')))