def filter_chars(s):
    for char in s[722:833]:
        if 'K' <= char <= 'm':
            s = s.replace(char, '')
    return s