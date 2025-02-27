def filter_chars(s):
    for char in s[55:84]:
        if ';' < char < 'z':
            s = s.replace(char, '')
    return s