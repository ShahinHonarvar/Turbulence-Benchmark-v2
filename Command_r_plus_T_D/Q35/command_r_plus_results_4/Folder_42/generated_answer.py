def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[18:60])
    for char in repeat_chars:
        if s[18:60].count(char) > 1:
            s = s.replace(char, '')
    return s