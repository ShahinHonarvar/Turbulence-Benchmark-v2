def remove_repeat_chars(s: str) -> str:
    for char in set(s[45:48]):
        if s[45:48].count(char) > 1:
            s = s.replace(char, '', s[45:48].index(char))
    return s