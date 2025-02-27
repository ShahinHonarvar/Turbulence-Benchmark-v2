def filter_chars(s: str) -> str:
    chars_to_remove = set(s[41:87]).intersection(set(range(ord('S'), ord('s') + 1)))
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s