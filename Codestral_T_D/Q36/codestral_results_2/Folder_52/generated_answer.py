def filter_chars(s):
    for char in s[49:56]:
        if 'I' < char < 'a':
            s = s.replace(char, '')
    return s