def filter_chars(s):
    for char in s[1:6]:
        if ',' < char < 'f':
            s = s.replace(char, '')
    return s