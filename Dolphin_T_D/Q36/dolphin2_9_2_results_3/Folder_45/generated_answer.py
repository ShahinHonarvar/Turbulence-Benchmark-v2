def filter_chars(s):
    for i in range(81, 86):
        char = s[i]
        if '!' < char < 's':
            s = s.replace(char, '')
    return s