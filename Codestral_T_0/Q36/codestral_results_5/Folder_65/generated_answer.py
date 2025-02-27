def filter_chars(s):
    for char in s[58:82]:
        if 'F' < char < 'O':
            s = s.replace(char, '')
    return s