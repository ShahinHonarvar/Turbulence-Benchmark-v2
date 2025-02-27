def remove_repeat_chars(s: str) -> str:
    for char in set(s[19:32]):
        if s[18:32].count(char) > 1:
            s = s.replace(char, '', s[18:32].index(char) + 18)
    return s