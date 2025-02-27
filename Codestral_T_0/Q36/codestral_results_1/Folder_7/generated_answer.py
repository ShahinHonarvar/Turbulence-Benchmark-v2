def filter_chars(s):
    for char in s[502:946]:
        if 'W' < char < 'y':
            s = s.replace(char, '')
    return s