def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[17:88])
    for char in chars_to_remove:
        if s[17:88].count(char) > 1:
            s = s.replace(char, '', s[17:88].index(char))
    return s