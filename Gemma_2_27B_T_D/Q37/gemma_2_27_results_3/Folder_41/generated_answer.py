def filter_chars(s):
    for i in range(26, 65):
        char = chr(i)
        if char >= 'V' and char <= 'o':
            s = s.replace(char, '')
    return s