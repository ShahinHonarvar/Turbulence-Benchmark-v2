def filter_chars(s):
    for char in s[58:81]:
        if '5' < char < '>':
            s = s.replace(char, '')
    return s