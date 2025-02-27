def remove_repeat_chars(s: str) -> str:
    for char in set(s[29:53]):
        if s[29:53].count(char) > 1:
            s = s[:29] + s[29:].replace(char, '', 1) + s[53:]
    return s