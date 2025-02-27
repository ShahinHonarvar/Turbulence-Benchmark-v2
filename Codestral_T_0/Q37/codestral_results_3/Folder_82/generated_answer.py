def filter_chars(s):
    for char in s[12:26]:
        if 'P' <= char <= 'x':
            s = s.replace(char, '')
    return s