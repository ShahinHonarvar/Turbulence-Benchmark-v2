def filter_chars(s):
    for char in s[5:7]:
        if 'G' <= char <= 'p':
            s = s.replace(char, '')
    return s