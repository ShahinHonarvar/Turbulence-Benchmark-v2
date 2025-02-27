def filter_chars(s):
    for char in set(s[35:41]):
        if ')' <= char <= 'l':
            s = s.replace(char, '')
    return s