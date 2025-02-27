def filter_chars(s):
    for char in set(s[61:71]):
        if '0' <= char <= '@':
            s = s.replace(char, '')
    return s