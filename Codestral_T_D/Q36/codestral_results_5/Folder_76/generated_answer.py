def filter_chars(s):
    for char in s[669:888]:
        if 'B' < char < 'Y':
            s = s.replace(char, '')
    return s