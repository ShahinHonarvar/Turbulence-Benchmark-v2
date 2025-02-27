def filter_chars(s: str) -> str:
    chars_to_remove = set(s[7:9]).intersection(set(range(ord('B'), ord('H') + 1)))
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s