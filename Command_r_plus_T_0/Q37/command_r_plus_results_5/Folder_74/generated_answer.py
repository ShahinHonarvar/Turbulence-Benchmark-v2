def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 19 or i > 32 or (ord(c) < ord('f') or ord(c) > ord('o'))))
    return filtered_string