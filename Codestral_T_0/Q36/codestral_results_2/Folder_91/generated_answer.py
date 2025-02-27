def filter_chars(s):
    for char in s[0:3]:
        if '$' < char < '?':
            s = s.replace(char, '')
    return s