def filter_chars(s: str) -> str:
    chars_to_remove = set(s[26:65]).intersection(set(range(ord('V'), ord('o') + 1)))
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s