def remove_repeat_chars(s):
    for char in set(s[20:200]):
        if s[20:200].count(char) > 1:
            s = s.replace(char, '', s[20:200].index(char))
    return s