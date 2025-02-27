def filter_chars(s):
    for i in range(41, 56):
        char = s[i]
        if 'Z' < char < 'c':
            s = s.replace(char, '')
    return s