def filter_chars(s: str) -> str:
    start, end = (154, 222)
    return ''.join((c for c in s if s.index(c) < start or s.index(c) >= end or (not 'A' < c < 'f')))