def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 299 > s.index(c) > 418 or not '9' < c < 'P'))