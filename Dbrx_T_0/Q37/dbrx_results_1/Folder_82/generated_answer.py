def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 12 or i > 25 or (c < 'P' or c > 'x')))