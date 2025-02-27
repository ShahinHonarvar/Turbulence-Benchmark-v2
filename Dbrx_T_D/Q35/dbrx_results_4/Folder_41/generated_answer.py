def remove_repeat_chars(s):
    for char in set(s[3:8]):
        if s[3:8].count(char) > 1:
            s = s.replace(char, '', s[3:8].index(char))
    return s