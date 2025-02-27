def filter_chars(s):
    for i in range(3, 5):
        char = s[i]
        if 'Y' < char < 's':
            s = s.replace(char, '', 1)
    return s