def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[36:54])
    for char in chars_to_remove:
        if s[36:54].count(char) > 1:
            s = s.replace(char, '', s[36:54].index(char))
    return s