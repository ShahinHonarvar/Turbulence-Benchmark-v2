def filter_chars(s):
    for char in set(s[24:80]):
        if 'a' <= char <= 'f':
            s = s.replace(char, '')
    return s