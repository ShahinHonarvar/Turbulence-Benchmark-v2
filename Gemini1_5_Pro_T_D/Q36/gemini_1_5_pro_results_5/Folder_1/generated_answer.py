def filter_chars(s):
    for i in range(69, 87):
        if i in range(ord('#') + 1, ord('L')):
            c = chr(i)
            s = s.replace(c, '')
    return s