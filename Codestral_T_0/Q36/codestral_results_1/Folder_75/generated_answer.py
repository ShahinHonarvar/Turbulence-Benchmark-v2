def filter_chars(s):
    for char in s[46:74]:
        if '&' < char < 'M':
            s = s.replace(char, '')
    return s