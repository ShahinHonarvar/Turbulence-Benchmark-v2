def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 323 or i >= 526 or ord(')') < ord(c) < ord('O')))