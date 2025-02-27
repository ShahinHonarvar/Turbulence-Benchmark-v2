def filter_chars(s):
    substring = s[344:874]
    for char in substring:
        if 'f' < char < '~':
            s = s.replace(char, '')
    return s