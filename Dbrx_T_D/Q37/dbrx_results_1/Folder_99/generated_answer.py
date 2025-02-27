def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 373 or i > 901 or (c < 'T' or c > 'h')))