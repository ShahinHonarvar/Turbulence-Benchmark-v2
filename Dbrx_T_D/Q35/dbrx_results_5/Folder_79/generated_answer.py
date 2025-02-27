def remove_repeat_chars(s: str) -> str:
    for i in range(1, 8):
        char = s[i]
        if s[1:8].count(char) > 1:
            s = s.replace(char, '', 1)
    return s