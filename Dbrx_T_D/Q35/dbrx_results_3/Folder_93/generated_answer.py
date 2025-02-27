def remove_repeat_chars(s):
    for char in set(s[57:85]):
        if s[57:85].count(char) > 1:
            s = s.replace(char, '', s[57:85].index(char))
    return s