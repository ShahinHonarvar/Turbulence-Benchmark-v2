def filter_chars(s):
    for char in sorted(s[15:85]):
        if 'I' < char < 'M':
            s = s.replace(char, '')
    return s