def filter_chars(s):
    for char in s[283:484]:
        if 'l' < char < 't':
            s = s.replace(char, '')
    return s