def filter_chars(s):
    for char in s[46:86]:
        if ord('-') <= ord(char) <= ord('X'):
            s = s.replace(char, '')
    return s