def filter_chars(s: str) -> str:
    chars_to_remove = set(range(ord(')') + 1, ord('l') + 1))[35:41]
    for char in chars_to_remove:
        s = s.replace(chr(char), '', 1)
    return s