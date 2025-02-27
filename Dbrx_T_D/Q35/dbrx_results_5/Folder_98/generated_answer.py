def remove_repeat_chars(s: str) -> str:
    for char in set(s[1:8]):
        if s[1:8].count(char) > 1:
            s = ''.join((char if i <= s[1:8].index(char) or i >= s[1:8].index(char) + s[1:8][s[1:8].index(char):].index(char) + 1 else '' for i, char in enumerate(s)))
    return s