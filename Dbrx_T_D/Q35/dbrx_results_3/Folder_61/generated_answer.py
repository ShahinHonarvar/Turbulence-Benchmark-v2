def remove_repeat_chars(s: str) -> str:
    for i in range(1, 9):
        char = s[i]
        if s[:i].count(char) > 0 or s[i:].count(char) > 1:
            s = s.replace(char, '', 1)
    return s