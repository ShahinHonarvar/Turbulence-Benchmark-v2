def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if 36 <= i <= 40 and 'H' <= c <= 'e' or i < 36 or i > 40))