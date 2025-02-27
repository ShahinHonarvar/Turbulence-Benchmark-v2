def filter_chars(s):
    for char in s[587:648]:
        if ',' < char < 'c':
            s = s.replace(char, '')
    return s