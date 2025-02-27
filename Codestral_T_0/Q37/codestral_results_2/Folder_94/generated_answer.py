def filter_chars(s):
    for char in sorted(set(s[51:97])):
        if 'X' <= char <= 'p':
            s = s.replace(char, '')
    return s