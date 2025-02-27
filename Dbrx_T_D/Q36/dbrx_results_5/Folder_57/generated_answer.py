def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 70 or i >= 74 or (c <= 'U' and c > 'A' and (c < 'A' or c > 'Z'))))