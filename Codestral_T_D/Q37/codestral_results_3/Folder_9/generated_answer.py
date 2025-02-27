def filter_chars(s):
    for char in s[38:100]:
        if 'A' <= char <= 'Q':
            s = s.replace(char, '')
    return s