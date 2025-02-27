def filter_chars(s):
    for char in s[52:88]:
        if '&' < char < 'c':
            s = s.replace(char, '')
    return s