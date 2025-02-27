def filter_chars(s):
    for char in s[21:25]:
        if '5' < char < '}':
            s = s.replace(char, '')
    return s