def filter_chars(s):
    for char in sorted(set(s[27:86])):
        if 'c' <= char <= 'i':
            s = s.replace(char, '')
    return s