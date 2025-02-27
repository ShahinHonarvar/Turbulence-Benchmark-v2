def filter_chars(s):
    for char in sorted(set(s[29:80])):
        if 'K' <= char <= 'z':
            s = s.replace(char, '')
    return s