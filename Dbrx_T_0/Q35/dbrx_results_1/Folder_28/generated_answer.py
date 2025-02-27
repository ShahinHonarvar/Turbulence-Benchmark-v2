def remove_repeat_chars(s: str) -> str:
    for char in set(s[86:99]):
        if s[86:99].count(char) > 1:
            s = s.replace(char, '', s[86:99].index(char))
    return s