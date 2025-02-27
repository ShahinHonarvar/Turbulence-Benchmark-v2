def remove_repeat_chars(s):
    indices = range(17, 88)
    for i in indices:
        char = s[i]
        if s.count(char) > 1:
            s = s.replace(char, '')
    return s