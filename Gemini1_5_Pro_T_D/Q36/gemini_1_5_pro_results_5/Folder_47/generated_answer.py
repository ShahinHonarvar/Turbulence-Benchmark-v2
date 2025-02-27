def filter_chars(s):
    for i in range(45, 57):
        if i >= ord('F') and i <= ord('n'):
            c = chr(i)
            s = s.replace(c, '')
    return s