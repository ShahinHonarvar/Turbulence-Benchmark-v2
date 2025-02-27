def filter_chars(s):
    for char in set(s[42:93]):
        if '/' <= char <= 'a':
            s = s.replace(char, '')
    return s