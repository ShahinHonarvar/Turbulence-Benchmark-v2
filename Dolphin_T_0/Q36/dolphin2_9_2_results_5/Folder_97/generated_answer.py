def filter_chars(s):
    for char in s[309:591]:
        if char > 'S' and char < 'm':
            s = s.replace(char, '')
    return s