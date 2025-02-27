def filter_chars(s):
    for char in s[86:93]:
        if 'E' < char < '~':
            s = s.replace(char, '')
    return s