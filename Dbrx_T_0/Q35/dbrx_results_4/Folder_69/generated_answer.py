def remove_repeat_chars(s: str) -> str:
    for char in set(s[39:43]):
        if s[39:43].count(char) > 1:
            s = s.replace(char, '', s[39:43].index(char))
    return s