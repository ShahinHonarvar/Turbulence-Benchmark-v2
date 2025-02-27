def filter_chars(s):
    for i in range(33, 84):
        char = chr(i)
        if 'm' < char < 'w':
            s = s.replace(char, '')
    return s