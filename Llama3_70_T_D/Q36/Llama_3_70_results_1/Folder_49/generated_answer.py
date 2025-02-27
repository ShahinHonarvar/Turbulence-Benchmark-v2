def filter_chars(s):
    chars = [chr(i) for i in range(46, 91)]
    for char in chars:
        if 'D' < char < 'H':
            s = s.replace(char, '')
    return s