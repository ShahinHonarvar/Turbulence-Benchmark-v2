def filter_chars(s: str) -> str:
    chars_to_remove = set(s[35:99]).intersection(set(range(ord('A'), ord('b') + 1)))
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s