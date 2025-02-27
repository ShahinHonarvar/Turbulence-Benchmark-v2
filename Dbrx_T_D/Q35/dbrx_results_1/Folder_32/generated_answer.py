def remove_repeat_chars(s):
    for i in range(86, 90):
        char = s[i]
        if s[i:].count(char) > 1:
            s = s.replace(char, '', s[i:].find(char))
    return s