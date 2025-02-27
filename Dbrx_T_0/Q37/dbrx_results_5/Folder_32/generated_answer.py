def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 23 or i > 89 or ord('w') <= ord(c) <= ord('{')))