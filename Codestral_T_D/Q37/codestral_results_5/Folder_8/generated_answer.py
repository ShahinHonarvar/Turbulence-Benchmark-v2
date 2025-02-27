def filter_chars(s):
    for char in sorted(s[41:87]):
        if 'S' <= char <= 's':
            s = s.replace(char, '')
    return s