def filter_chars(s):
    for c in range(43, 83):
        char = chr(c)
        if ':' < char < 'Q':
            s = s.replace(char, '')
    return s