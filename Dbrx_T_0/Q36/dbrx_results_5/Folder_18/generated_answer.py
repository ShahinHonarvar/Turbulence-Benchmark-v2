def filter_chars(s: str) -> str:
    return ''.join((c for c in s[587:648] if c <= ',' or c >= 'c')) + s[:587] + s[648:]