def filter_chars(s):
    for char in s[309:591]:
        if 'S' < char < 'm':
            s = s.replace(char, '')
    return s