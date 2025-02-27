def remove_repeat_chars(s):
    for char in set(s[32:44]):
        if s[32:44].count(char) > 1:
            s = s.replace(char, '', s[32:44].index(char))
    return s