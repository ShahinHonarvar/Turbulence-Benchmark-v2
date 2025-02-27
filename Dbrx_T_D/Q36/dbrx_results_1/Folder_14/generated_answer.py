def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if not (41 < i < 56 and 'Z' < c < 'c')))