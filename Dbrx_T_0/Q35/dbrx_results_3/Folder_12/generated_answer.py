def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[16:87])
    for char in chars_to_remove:
        if s[16:87].count(char) > 1:
            s = s.replace(char, '', s[16:87].index(char))
    return s