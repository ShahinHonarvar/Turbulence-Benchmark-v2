def filter_chars(s):
    for i in range(7, 10):
        char = s[i]
        if '6' <= char <= 'w':
            s = s.replace(char, '')
    return s