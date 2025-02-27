def filter_chars(s: str) -> str:
    return ''.join((c for c in s if s.index(c) < 4 and '$' < c < '?'))