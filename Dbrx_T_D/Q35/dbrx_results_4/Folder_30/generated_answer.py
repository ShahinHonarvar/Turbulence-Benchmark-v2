def remove_repeat_chars(s: str) -> str:
    for char in s[22:24]:
        if s[22:24].count(char) > 1:
            s = s.replace(char, '', s[22:24].index(char))
    return s