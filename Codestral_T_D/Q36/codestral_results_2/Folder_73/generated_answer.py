def filter_chars(s):
    for char in s[66:90]:
        if char > '#' and char < 'T':
            s = s.replace(char, '')
    return s