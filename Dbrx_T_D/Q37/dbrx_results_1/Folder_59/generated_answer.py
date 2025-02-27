def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 2 or i > 3 or (not '5' <= c <= '_')))