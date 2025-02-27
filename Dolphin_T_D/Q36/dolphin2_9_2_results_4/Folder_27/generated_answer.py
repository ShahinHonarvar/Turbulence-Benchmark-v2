def filter_chars(s):
    for c in range(48, 75):
        if '6' < chr(c) < '_':
            s = ''.join([i for i in s if i != chr(c)])
    return s