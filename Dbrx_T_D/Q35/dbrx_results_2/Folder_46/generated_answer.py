def remove_repeat_chars(s: str) -> str:
    for char in set(s[1:10]):
        if s[1:10].count(char) > 1:
            s = s.replace(char, '', s[1:10].index(char))
    return s