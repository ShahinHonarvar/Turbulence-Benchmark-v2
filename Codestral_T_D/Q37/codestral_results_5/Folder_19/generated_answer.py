def filter_chars(s):
    for char in s[35:90]:
        if 'E' <= char <= 't':
            s = s.replace(char, '')
    return s