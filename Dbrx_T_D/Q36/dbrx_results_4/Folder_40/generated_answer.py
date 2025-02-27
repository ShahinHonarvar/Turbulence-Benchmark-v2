def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 1 or i >= 7 or (c > '-' and c < 'L')))