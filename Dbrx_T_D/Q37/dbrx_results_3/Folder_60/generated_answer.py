def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 12 or i > 77 or ord(':') <= ord(c) <= ord('L')))