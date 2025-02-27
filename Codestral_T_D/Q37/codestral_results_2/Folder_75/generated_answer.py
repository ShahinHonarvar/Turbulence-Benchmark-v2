def filter_chars(s):
    for char in sorted(set(s[34:68])):
        if 'W' <= char <= 'x':
            s = s.replace(char, '')
    return s