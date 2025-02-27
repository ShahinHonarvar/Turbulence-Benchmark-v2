def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[20:35]) & set(s[20:35])
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s