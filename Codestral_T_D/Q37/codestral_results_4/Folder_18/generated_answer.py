def filter_chars(s):
    for char in set(s[770:971]):
        if '-' <= char <= 'D':
            s = s.replace(char, '')
    return s