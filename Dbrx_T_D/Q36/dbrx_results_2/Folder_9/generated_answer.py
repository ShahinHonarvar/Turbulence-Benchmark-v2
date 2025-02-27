def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 50 or i >= 92 or (c <= 'A' or c >= 'Q')))