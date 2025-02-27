def remove_repeat_chars(s: str) -> str:
    for char in set(s[1:5]):
        if s[1:5].count(char) > 1:
            s = s.replace(char, '', s[1:5].index(char))
    return s