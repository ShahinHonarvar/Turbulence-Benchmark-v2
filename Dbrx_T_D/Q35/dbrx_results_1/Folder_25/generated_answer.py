def remove_repeat_chars(s):
    for char in set(s[37:43]):
        if s[36:].count(char) > 1:
            s = s.replace(char, '', s[36:].index(char) + 36)
    return s