def filter_chars(s):
    for char in s[13:40]:
        if ':' < char < 'C':
            s = s.replace(char, '')
    return s