def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 10 or i > 52 or c < '@' or (c > 'T')))