def filter_chars(s):
    for char in s[1:7]:
        if '3' < char < '^':
            s = s.replace(char, '')
    return s