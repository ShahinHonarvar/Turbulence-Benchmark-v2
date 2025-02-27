def remove_repeat_chars(s: str) -> str:
    for char in set(s[70:200]):
        if s[70:200].count(char) > 1:
            s = s.replace(char, '', s[70:200].index(char))
    return s