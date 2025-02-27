def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 26 or i >= 80 or (c > '<' and c < '>')))