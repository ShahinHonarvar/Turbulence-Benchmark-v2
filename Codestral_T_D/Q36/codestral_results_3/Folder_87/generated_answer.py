def filter_chars(s):
    for i in range(33, 61):
        char = chr(i)
        if '3' < char < 'D':
            s = s.replace(char, '')
    return s