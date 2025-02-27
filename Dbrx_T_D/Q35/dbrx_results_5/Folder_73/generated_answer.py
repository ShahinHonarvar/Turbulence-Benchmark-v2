def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[10:76]).intersection(s[:10] + s[76:])
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s