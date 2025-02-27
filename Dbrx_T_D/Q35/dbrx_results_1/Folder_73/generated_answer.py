def remove_repeat_chars(s):
    for char in set(s[10:76]):
        if s[10:76].count(char) > 1:
            s = s.replace(char, '', s[10:76].index(char))
    return s