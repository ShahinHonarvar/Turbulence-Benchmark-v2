def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 3 or i >= 8 or (c > '?' and c < 'k')))