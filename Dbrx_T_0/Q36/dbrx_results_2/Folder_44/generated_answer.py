def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 18 or i > 64 or ord('3') < ord(c) < ord('B')))