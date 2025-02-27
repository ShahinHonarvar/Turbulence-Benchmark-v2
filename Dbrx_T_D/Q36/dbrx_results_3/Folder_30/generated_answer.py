def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 23 or i >= 45 or (not '3' < c < 'I')))