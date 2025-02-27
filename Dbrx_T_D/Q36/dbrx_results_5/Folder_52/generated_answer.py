def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 49 or i > 56 or (c > 'I' and c < 'a')))