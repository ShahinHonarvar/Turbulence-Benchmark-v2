def filter_chars(s):
    for char in s[71:95]:
        if 'K' <= char <= 'a':
            s = s.replace(char, '')
    return s