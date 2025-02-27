def filter_chars(s):
    for i in range(52, 88):
        char = s[i]
        if char > '&' and char < 'c':
            s = s.replace(char, '')
    return s