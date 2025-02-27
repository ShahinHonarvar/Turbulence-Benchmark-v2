def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 36 or i > 79 or (ord(c) < ord('a') or ord(c) > ord('i'))))
    return filtered_string