def filter_chars(s):
    for char in s[31:70]:
        if 'B' < char < 'v':
            s = s.replace(char, '')
    return s