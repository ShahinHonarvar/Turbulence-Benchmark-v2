def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 43 or i >= 69 or (not 'B' < c < 'r')))