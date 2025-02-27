def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 56 or i > 86 or ord('+') < ord(c) < ord('w')))