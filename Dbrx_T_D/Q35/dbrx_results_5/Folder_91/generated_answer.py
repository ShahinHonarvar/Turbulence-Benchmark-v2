def remove_repeat_chars(s):
    for char in set(s[1:7]):
        if s[1:7].count(char) > 1:
            s = s.replace(char, '', 1)
    return s