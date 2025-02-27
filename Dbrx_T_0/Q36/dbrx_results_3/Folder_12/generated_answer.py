def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 32 < ord(c) < 84 or not 'm' < c < 'w'))