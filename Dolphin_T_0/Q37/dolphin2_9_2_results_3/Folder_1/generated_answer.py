def filter_chars(s):
    for char in s[41:80]:
        if 'f' <= char <= '|':
            s = s.replace(char, '')
    return s