def filter_chars(s):
    for char in s[23:83]:
        if 'f' < char < 'o':
            s = s.replace(char, '')
    return s