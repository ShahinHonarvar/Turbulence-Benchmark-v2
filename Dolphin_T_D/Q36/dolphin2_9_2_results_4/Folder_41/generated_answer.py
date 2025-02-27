def filter_chars(s):
    for char in set(s[81:89]):
        if 'f' < char < '{':
            s = s.replace(char, '')
    return s