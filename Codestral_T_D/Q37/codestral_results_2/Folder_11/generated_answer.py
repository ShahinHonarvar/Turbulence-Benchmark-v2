def filter_chars(s):
    for char in s[29:98]:
        if '-' <= char <= 'n':
            s = s.replace(char, '')
    return s