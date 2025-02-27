def filter_chars(s):
    for char in s[42:68]:
        if 't' < char < 'x':
            s = s.replace(char, '')
    return s