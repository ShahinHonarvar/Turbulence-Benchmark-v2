def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if c < '>' or c > 'A' or i < 33 or (i >= 36)))