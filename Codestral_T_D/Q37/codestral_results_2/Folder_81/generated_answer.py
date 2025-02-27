def filter_chars(s):
    for char in sorted(set(s[19:93])):
        if '8' <= char <= 'm':
            s = s.replace(char, '')
    return s