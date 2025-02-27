def remove_repeat_chars(s):
    for char in set(s[86:90]):
        if s[86:90].count(char) > 1:
            s = s.replace(char, '', s[86:90].index(char))
    return s