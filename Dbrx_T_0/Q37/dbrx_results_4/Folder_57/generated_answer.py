def filter_chars(s: str) -> str:
    chars_to_remove = set(s[27:85]).intersection(set(range(ord('!'), ord('B') + 1)))
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s