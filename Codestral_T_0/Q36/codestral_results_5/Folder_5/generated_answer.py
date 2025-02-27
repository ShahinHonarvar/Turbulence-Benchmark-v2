def filter_chars(s):
    for char in s[55:66]:
        if 'f' < char < '|':
            s = s.replace(char, '')
    return s