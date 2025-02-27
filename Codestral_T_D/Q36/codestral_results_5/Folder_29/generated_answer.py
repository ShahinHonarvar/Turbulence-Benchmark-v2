def filter_chars(s):
    for char in s[46:68]:
        if 'H' < char < 's':
            s = s.replace(char, '')
    return s