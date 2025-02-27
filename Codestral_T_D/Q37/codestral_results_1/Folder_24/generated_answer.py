def filter_chars(s):
    for i in range(36, 80):
        char = s[i]
        if '2' <= char <= 's':
            s = s.replace(char, '')
    return s