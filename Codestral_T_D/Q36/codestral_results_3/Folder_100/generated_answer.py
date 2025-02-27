def filter_chars(s):
    for char in s[43:70]:
        if 'B' < char < 'r':
            s = s.replace(char, '')
    return s