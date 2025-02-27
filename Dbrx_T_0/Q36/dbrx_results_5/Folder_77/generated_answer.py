def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 221 or i > 419 or (c > '-' and c < 'v')))