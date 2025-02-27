def filter_chars(s):
    for i in range(38, 55):
        char = s[i]
        if ':' <= char <= 'r':
            s = s.replace(char, '')
    return s