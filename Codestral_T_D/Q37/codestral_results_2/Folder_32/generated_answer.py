def filter_chars(s):
    for char in s[23:90]:
        if 'w' <= char <= '{':
            s = s.replace(char, '')
    return s