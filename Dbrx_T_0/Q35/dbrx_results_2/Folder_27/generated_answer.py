def remove_repeat_chars(s: str) -> str:
    for char in set(s[86:89]):
        if s[86:89].count(char) > 1:
            s = s.replace(char, '', s[86:89].index(char))
    return s