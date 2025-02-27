def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 11 or i > 72 or ord('i') <= ord(c) <= ord('v')))