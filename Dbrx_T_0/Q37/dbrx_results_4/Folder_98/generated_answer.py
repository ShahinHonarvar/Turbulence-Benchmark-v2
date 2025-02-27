def filter_chars(s: str) -> str:
    chars_to_remove = set(s[8:10]).intersection(set(range(ord('R'), ord('t') + 1)))
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s