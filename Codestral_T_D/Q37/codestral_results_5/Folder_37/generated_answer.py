def filter_chars(s):
    for char in set(s[17:64]):
        if 'O' <= char <= '^':
            s = s.replace(char, '')
    return s