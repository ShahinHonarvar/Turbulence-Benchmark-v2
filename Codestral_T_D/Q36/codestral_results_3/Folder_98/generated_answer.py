def filter_chars(s):
    for char in s[4:8]:
        if '1' < char < 'J':
            s = s.replace(char, '')
    return s