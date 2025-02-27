def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 43 or i > 58 or (ord(c) > ord('5') and ord(c) < ord('C'))))