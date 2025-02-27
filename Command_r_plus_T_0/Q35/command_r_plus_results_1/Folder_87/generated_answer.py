def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[20:43])
    for char in repeat_chars:
        s = s.replace(char, '', s.count(char))
    return s