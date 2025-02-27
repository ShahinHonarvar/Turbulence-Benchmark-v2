def filter_chars(s: str) -> str:
    chars_to_filter = set(range(86, 93)) & set(range(ord('E') + 1, ord('~') + 1, -1))
    for char in chars_to_filter:
        s = s.replace(chr(char), '')
    return s