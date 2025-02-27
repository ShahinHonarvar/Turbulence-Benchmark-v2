def remove_repeat_chars(s):
    for char in set(s[6:9]):
        if s[6:9].count(char) > 1:
            s = s.replace(char, '', s[6:9].index(char))
    return s