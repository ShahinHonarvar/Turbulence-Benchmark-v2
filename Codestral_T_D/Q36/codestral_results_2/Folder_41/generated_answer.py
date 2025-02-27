def filter_chars(s):
    for char in s[81:89]:
        if 'f' < char < '{':
            s = s.replace(char, '')
    return s