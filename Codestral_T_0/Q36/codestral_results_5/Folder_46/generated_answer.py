def filter_chars(s):
    for char in s[19:69]:
        if '<' < char < 'C':
            s = s.replace(char, '')
    return s