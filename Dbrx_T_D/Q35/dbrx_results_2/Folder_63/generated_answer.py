def remove_repeat_chars(s):
    for char in set(s[81:86]):
        if s[81:86].count(char) > 1:
            s = s.replace(char, '', s[81:86].index(char))
    return s