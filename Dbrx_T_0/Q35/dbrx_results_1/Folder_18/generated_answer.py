def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[56:90])
    for char in chars_to_remove:
        if s[56:90].count(char) > 1:
            s = s.replace(char, '', s[56:90].index(char))
    return s