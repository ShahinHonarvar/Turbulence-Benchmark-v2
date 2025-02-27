def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[18:60])
    for char in chars_to_remove:
        if s[18:60].count(char) > 1:
            s = s.replace(char, '', s[18:60].index(char))
    return s