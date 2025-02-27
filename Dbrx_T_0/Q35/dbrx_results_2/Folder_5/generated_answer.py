def remove_repeat_chars(s: str) -> str:
    for char in set(s[2:8]):
        if s[2:8].count(char) > 1:
            s = s.replace(char, '', s[2:8].index(char))
    return s