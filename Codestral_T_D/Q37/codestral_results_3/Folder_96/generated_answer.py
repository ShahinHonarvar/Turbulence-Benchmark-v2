def filter_chars(s):
    for char in s[86:93]:
        if '!' <= char <= 's':
            s = s.replace(char, '')
    return s