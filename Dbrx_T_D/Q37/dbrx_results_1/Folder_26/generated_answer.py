def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 20 or i > 62 or (ord('i') <= ord(c) <= ord('k')) is False))