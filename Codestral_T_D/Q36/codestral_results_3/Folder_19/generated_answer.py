def filter_chars(s):
    for char in s[77:87]:
        if ';' < char < 'r':
            s = s.replace(char, '')
    return s