def filter_chars(s):
    for char in s[344:874]:
        if char > 'f' and char < '~':
            s = s.replace(char, '')
    return s