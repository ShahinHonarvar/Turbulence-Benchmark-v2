def filter_chars(s):
    for char in s[24:37]:
        if 'A' < char < 'h':
            s = s.replace(char, '')
    return s