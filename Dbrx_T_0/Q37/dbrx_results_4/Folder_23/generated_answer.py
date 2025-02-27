def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 51 or i > 77 or (c < 'V' or c > 'Y')))