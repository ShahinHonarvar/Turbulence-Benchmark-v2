def remove_repeat_chars(s: str) -> str:
    for char in set(s[40:200]):
        if s[40:200][char].count(char) > 1:
            s = s.replace(char, '', s[40:200].index(char))
            s = s[:40] + s[40:].replace(char, '', 1)
    return s