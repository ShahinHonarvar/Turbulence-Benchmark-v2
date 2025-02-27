def filter_chars(s):
    for i in range(48, 75):
        char = chr(i)
        if '6' < char < '_':
            s = s.replace(char, '')
    return s