def remove_repeat_chars(s):
    for char in set(s[43:70]):
        if s.count(char) > 1:
            s = s.replace(char, '', s.count(char))
    return s