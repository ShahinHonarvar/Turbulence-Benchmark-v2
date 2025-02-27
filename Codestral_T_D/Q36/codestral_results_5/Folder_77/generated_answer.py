def filter_chars(s):
    for char in s[221:419]:
        if '-' < char < 'v':
            s = s.replace(char, '')
    return s