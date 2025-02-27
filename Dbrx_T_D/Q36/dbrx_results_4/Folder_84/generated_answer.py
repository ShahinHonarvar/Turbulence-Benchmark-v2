def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 171 or i >= 636 or (not 'c' < c < 's')))