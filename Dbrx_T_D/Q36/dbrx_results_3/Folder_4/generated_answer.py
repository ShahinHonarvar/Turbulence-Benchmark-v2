def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 42 or i > 65 or (not 54 < ord(c) < 103)))