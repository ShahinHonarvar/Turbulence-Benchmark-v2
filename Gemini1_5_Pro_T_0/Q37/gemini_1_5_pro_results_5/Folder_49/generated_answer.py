def filter_chars(s):
    for i in range(42, 98):
        if i >= ord('*') and i <= ord('b'):
            c = chr(i)
            s = s.replace(c, '')
    return s