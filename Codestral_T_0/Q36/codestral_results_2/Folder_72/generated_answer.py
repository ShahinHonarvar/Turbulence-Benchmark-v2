def filter_chars(s):
    for char in s[44:68]:
        if 'W' < char < 'x':
            s = s.replace(char, '')
    return s