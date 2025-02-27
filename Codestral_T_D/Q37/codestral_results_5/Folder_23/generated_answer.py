def filter_chars(s):
    for char in sorted(set(s[51:78])):
        if 'V' <= char <= 'Y':
            s = s.replace(char, '')
    return s