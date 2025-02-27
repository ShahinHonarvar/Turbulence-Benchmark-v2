def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 41 or i >= 56 or (not 'Z' < c < 'c'))) if s else ''