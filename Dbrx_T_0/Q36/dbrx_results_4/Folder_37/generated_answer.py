def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 47 < ord(c) < 54 or 44 > ord(c) > 59))