def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[49:74])
    for char in chars_to_remove:
        if s[49:74].count(char) > 1:
            s = s.replace(char, '', s[49:74].index(char) + 49)
    return s