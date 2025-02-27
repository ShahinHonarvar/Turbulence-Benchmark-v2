def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 31 < s.index(c) < 73 and 'M' < c < 'j'))