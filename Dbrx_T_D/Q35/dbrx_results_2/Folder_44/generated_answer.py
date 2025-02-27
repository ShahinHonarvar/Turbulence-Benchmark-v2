def remove_repeat_chars(s: str) -> str:
    for char in set(s[36:52]):
        if s[36:52].count(char) > 1:
            s = s.replace(char, '', s[36:52].index(char))
    return s