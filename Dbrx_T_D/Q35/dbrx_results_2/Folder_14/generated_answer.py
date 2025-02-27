def remove_repeat_chars(s: str) -> str:
    for char in s[2:5]:
        if s[2:5].count(char) > 1:
            s = s.replace(char, '', s[2:5].index(char))
    return s