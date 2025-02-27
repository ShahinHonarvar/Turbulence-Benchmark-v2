def remove_repeat_chars(s):
    for char in set(s[13:91]):
        if s[13:91].count(char) > 1:
            s = s.replace(char, '')
    return s