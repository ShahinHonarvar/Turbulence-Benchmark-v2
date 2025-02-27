def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 221 < s.index(c) < 419 or not '-' < c < 'v'))