def remove_repeat_chars(s: str) -> str:
    for i in range(2, 5):
        char = s[i]
        if s[i + 1:].count(char) > 0:
            s = s.replace(char, '', s[i + 1:].index(char))
    return s