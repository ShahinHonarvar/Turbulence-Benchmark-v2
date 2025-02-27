def remove_repeat_chars(s: str) -> str:
    for char in set(s[38:52]):
        if s[38:52].count(char) > 1:
            s = s.replace(char, '', s[38:52].index(char))
    return s