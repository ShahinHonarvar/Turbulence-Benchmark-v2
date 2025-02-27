def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 43 or i >= 59 or (not '5' < c < 'C')))