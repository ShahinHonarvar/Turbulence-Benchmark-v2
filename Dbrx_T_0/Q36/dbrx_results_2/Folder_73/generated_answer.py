def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 66 < ord(c) < 90 and (not '#' < c < 'T')))