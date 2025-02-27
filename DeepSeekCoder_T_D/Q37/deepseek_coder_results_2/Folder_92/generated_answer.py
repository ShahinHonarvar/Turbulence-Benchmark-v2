def filter_chars(s):
    for char in s[4:5]:
        if '7' <= char <= 'o':
            s = s.replace(char, '')
    return s