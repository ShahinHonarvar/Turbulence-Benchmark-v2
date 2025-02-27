def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 421 or i >= 854 or (not 'D' < c < 'J')))[420:854]