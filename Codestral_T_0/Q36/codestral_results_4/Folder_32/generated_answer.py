def filter_chars(s):
    for char in s[40:63]:
        if '7' < char < 'H':
            s = s.replace(char, '')
    return s