def remove_repeat_chars(s):
    for char in set(s[200:202]):
        if s[200:202].count(char) > 1:
            s = s.replace(char, '', s[200:202].index(char))
    return s