def filter_chars(s):
    for char in set(s[379:899]):
        if 'M' <= char <= 'v':
            s = s.replace(char, '')
    return s