def filter_chars(s):
    for i in range(46, 86):
        if i >= ord('-') and i <= ord('X'):
            char = chr(i)
            s = s.replace(char, '')
    return s