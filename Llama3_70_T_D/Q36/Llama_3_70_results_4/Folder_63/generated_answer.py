def filter_chars(s):
    for char in s[26:80]:
        if '<' < char < '>':
            s = s.replace(char, '')
    return s