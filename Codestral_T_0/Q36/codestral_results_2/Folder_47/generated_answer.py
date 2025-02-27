def filter_chars(s):
    for char in s[45:57]:
        if 'F' < char < 'n':
            s = s.replace(char, '')
    return s