def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 36 or i > 79 or ord('i') >= ord(c) >= ord('a')))