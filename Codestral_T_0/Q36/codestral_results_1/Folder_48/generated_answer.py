def filter_chars(s):
    for char in s[154:222]:
        if 'A' < char < 'f':
            s = s.replace(char, '')
    return s