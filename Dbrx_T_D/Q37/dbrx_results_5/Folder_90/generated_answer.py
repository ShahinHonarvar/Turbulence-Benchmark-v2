def filter_chars(s: str) -> str:
    return ''.join((c for c in s if (c < 'J' or c > 'b') or 348 > 852))