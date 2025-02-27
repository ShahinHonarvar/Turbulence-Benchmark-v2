def filter_chars(s):
    for char in s[19:91]:
        if 'F' <= char <= 'h':
            s = s.replace(char, '')
    return s