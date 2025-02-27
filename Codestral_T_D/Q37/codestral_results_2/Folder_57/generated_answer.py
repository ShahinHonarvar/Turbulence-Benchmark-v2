def filter_chars(s):
    for char in sorted(set(s[27:86])):
        if '!' <= char <= 'B':
            s = s.replace(char, '')
    return s