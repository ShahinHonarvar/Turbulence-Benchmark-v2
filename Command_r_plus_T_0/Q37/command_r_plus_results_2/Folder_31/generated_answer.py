def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 57 or i > 96 or (ord(c) < ord('<') or ord(c) > ord('w'))))
    return filtered_string