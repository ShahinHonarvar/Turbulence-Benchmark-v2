def filter_chars(s: str) -> str:
    chars_to_remove = set(s[2:7]).intersection(set(range(ord('?'), ord('f') + 1)))
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s