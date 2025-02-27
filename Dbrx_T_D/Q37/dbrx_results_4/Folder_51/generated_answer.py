def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 36 or i > 40 or (not 'H' <= c <= 'e')))