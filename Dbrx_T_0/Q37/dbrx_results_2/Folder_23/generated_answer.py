def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if not (51 <= i <= 77 and 'V' <= c <= 'Y')))