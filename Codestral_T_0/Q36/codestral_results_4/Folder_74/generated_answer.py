def filter_chars(s):
    for char in s[33:36]:
        if '>' < char < 'A':
            s = s.replace(char, '')
    return s