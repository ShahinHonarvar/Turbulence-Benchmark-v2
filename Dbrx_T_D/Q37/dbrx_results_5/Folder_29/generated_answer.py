def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if not (12 <= i <= 88 and 'v' >= c >= '&')))