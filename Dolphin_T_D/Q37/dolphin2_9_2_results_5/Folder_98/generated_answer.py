def filter_chars(s):
    for char in s[8:10]:
        if 'R' <= char <= 't':
            s = s.replace(char, '')
    return s