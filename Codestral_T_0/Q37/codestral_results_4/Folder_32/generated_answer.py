def filter_chars(s):
    for char in sorted(set(s[23:90])):
        if 'w' <= char <= '{':
            s = s.replace(char, '')
    return s