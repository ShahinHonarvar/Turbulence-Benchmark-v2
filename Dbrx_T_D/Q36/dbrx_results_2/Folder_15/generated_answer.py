def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 2 or i >= 7 or (not 'h' < c < 'k'))) if s else ''