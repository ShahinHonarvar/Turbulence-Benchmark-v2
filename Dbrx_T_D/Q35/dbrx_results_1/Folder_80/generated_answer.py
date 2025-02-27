def remove_repeat_chars(s: str) -> str:
    for char in set(s[57:84]):
        if s[57:84].count(char) > 1:
            s = s.replace(char, '', s[57:84].index(char))
    return s