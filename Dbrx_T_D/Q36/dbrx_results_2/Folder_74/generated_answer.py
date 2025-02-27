def filter_chars(s):
    for i in range(33, 36):
        char = chr(i)
        if '>' < char < 'A':
            s = s.replace(char, '', 1)
    return s