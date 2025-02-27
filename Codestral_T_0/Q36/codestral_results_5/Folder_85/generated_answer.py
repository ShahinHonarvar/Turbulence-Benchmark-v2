def filter_chars(s):
    for char in s[55:80]:
        if 'S' < char < 's':
            s = s.replace(char, '')
    return s