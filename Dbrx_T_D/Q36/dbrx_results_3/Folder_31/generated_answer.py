def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 14 or i >= 75 or ord('9') < ord(c) < ord('K')))