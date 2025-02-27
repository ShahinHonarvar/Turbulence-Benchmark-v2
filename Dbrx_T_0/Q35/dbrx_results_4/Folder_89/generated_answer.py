def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[55:84])
    for char in chars_to_remove:
        if s[55:84].count(char) > 1:
            s = s.replace(char, '', s[55:84].index(char))
    return s