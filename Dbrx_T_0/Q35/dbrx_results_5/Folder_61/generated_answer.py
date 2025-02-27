def remove_repeat_chars(s: str) -> str:
    for char in set(s[1:9]):
        if s[1:9].count(char) > 1:
            s = s.replace(char, '', s[1:9].index(char))
    return s