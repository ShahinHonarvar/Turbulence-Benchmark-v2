def filter_chars(s):
    for char in s[2:7]:
        if 'h' < char < 'k':
            s = s.replace(char, '')
    return s