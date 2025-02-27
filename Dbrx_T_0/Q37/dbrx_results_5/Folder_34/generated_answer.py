def filter_chars(s: str) -> str:
    chars_to_remove = set(s[54:63]).intersection(set(range(ord(')'), ord('9') + 1)))
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s