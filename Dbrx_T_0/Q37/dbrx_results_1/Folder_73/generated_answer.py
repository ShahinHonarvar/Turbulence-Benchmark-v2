def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 22 or i > 85 or ord('7') <= ord(c) <= ord('e')))