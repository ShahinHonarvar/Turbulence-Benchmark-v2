def filter_chars(s):
    for char in s[42:67]:
        if '6' < char < 'g':
            s = s.replace(char, '')
    return s