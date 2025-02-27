def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 343 or i > 665 or (c > '%' and c < 'U')))