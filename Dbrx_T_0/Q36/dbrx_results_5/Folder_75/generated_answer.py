def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 46 < s.index(c) < 74 and (not '&' < c < 'M')))