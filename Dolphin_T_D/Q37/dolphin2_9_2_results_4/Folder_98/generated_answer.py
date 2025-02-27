def filter_chars(s):
    for char in s[8:10]:
        if char >= 'R' and char <= 't':
            s = s.replace(char, '')
    return s