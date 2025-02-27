def filter_chars(s):
    for char in s[331:713]:
        if 'M' < char < '_':
            s = s.replace(char, '')
    return s