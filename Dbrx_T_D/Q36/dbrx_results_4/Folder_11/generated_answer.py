def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 86 or i >= 93 or (not 'E' < c < '~')))