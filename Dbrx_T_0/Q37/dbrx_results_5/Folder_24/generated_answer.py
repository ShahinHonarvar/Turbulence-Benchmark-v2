def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if 36 <= i <= 79 and '2' <= c <= 's'))