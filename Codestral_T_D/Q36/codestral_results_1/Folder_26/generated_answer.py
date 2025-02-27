def filter_chars(s):
    for char in s[43:83]:
        if ':' < char < 'Q':
            s = s.replace(char, '')
    return s