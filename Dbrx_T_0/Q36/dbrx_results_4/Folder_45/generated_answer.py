def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 33 < ord(c) < 115 or 81 > ord(c) > 86))