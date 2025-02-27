def filter_chars(s):
    for char in s[343:665]:
        if '%' < char < 'U':
            s = s.replace(char, '')
    return s