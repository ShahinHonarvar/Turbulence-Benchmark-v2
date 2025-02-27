def filter_chars(s):
    for char in s[28:66]:
        if 'O' <= char <= 'd':
            s = s.replace(char, '')
    return s