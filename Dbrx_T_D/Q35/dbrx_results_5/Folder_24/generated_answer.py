def remove_repeat_chars(s: str) -> str:
    for char in set(s[13:91]):
        if s[13:91].count(char) > 1:
            s = s.replace(char, '', s[13:91].index(char))
    return s