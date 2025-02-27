def filter_chars(s):
    for char in s[70:74]:
        if 'A' < char < 'U':
            s = s.replace(char, '')
    return s