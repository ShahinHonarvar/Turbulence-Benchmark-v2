def filter_chars(s: str) -> str:
    start, end = (309, 591)
    return ''.join((c for c in s if c < 'S' or c > 'm' or s.index(c) < start or (s.index(c) >= end)))