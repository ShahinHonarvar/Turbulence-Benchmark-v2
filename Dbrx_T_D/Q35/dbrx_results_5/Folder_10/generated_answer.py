def remove_repeat_chars(s):
    for char in set(s[36:54]):
        if s[36:54].count(char) > 1:
            s = s.replace(char, '', s[36:54].index(char))
    return s