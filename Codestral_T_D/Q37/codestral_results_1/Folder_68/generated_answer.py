def filter_chars(s):
    for char in s[7:10]:
        if '6' <= char <= 'w':
            s = s.replace(char, '')
    return s