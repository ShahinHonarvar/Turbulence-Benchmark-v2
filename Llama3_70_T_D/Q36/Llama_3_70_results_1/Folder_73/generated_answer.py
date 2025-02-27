def filter_chars(s):
    for i in range(66, 90):
        char = chr(i)
        if char > '#' and char < 'T':
            s = s.replace(char, '')
    return s