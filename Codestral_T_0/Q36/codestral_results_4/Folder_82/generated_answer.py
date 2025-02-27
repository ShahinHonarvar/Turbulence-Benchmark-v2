def filter_chars(s):
    for char in s[69:97]:
        if 'V' < char < 'j':
            s = s.replace(char, '')
    return s