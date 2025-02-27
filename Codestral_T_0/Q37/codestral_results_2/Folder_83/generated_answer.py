def filter_chars(s):
    for char in s[29:80]:
        if 'K' <= char <= 'z':
            s = s.replace(char, '')
    return s