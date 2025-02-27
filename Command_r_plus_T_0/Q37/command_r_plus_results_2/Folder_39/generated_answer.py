def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 52 or i > 81 or (ord(c) < ord('A') or ord(c) > ord('U'))))
    return filtered_string