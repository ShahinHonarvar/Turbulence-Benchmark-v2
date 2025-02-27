def remove_repeat_chars(s):
    for char in set(s[7:9]):
        if s[7:9].count(char) > 1:
            s = s.replace(char, '', s[7:9].index(char))
    return s