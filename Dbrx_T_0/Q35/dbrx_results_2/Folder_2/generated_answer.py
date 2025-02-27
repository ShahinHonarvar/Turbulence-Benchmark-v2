def remove_repeat_chars(s: str) -> str:
    for char in set(s[72:93]):
        if s[72:93].count(char) > 1:
            s = s.replace(char, '', s[72:93].index(char))
    return s