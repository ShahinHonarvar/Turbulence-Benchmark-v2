def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[36:52])
    for char in chars_to_remove:
        if s[36:52].count(char) > 1:
            s = s.replace(char, '', s[36:52].index(char))
    return s