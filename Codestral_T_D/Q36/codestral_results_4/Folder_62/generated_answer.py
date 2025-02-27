def filter_chars(s):
    for char in s[63:89]:
        if '*' < char < 'w':
            s = s.replace(char, '')
    return s