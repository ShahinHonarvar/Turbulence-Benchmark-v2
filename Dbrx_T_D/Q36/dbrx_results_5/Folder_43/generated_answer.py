def filter_chars(s: str) -> str:
    return ''.join((c for c in s if not (27 < s.index(c) < 75 and 'A' < c < 'i')))