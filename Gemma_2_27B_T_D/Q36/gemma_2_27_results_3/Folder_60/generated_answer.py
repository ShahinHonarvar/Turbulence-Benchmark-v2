def filter_chars(s):
    for i in range(23, 83):
        char = s[i]
        if char > 'f' and char < 'o':
            s = s.replace(char, '')
    return s