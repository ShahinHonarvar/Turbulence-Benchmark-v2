def remove_repeat_chars(s: str) -> str:
    for char in set(s[1:3]):
        if s[1:3].count(char) > 1:
            s = s.replace(char, '', 2)
    return s