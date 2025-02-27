def filter_chars(s):
    middle_chars = s[4:5]
    for char in middle_chars:
        if 'Y' < char < 's':
            s = s.replace(char, '')
    return s