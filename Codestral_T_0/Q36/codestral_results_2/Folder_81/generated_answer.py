def filter_chars(s):
    for char in s[51:76]:
        if '5' < char < 'f':
            s = s.replace(char, '')
    return s