def filter_chars(s):
    for char in s[512:877]:
        if '?' <= char <= 'n':
            s = s.replace(char, '')
    return s