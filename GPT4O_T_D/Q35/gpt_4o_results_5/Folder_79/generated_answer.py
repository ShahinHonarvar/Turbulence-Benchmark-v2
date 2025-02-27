def remove_repeat_chars(s):
    if len(s) <= 2:
        return s
    for char in set(s[2:7]):
        if s[2:7].count(char) > 1:
            s = s.replace(char, '')
    return s