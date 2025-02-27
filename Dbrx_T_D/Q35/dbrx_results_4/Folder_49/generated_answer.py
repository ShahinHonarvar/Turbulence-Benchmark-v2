def remove_repeat_chars(s: str) -> str:
    for char in set(s[90:200]):
        if s[90:200].count(char) > 1:
            s = s.replace(char, '', s[90:200].index(char))
    return s