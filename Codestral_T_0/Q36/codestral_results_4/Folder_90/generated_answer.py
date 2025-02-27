def filter_chars(s):
    for char in s[344:874]:
        if 'f' < char < '~':
            s = s.replace(char, '')
    return s