def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 24 or i >= 37 or (c > 'A' and c < 'h')))