def filter_chars(s: str) -> str:
    return ''.join((c for c in s if 72 > ord(c) > 115 or (ord(c) < 46 or ord(c) > 68) for c in s))