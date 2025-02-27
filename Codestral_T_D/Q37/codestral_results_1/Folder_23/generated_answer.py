def filter_chars(s):
    for char in set(s[51:78]):
        if 'V' <= char <= 'Y':
            s = s.replace(char, '')
    return s