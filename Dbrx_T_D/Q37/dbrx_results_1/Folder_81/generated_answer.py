def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if 19 <= i <= 92 and (not '8' <= c <= 'm')))