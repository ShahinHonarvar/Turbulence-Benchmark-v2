def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 48 < ord(c) < 75 or not '6' < c < '_'))